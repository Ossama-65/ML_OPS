import mlflow
import click
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
import lib.utils as ut
import os
import boto3

@click.command(help="Model prediction")
@click.option("--name", default="", help="Name of model")
@click.option("--model", default="latest", help="Model to be used")
@click.option("--environment", default="local", help="Production (prod) or Developer (dev) environment")

def create_prediction(environment, name, model):
    try:
        # 1. Set the bucket variable depending on the environment option
        bucket = ut.get_bucket_from_env(environment)
        path = 'data'
        print(f"- Using bucket as:\n{bucket if bucket != '' else 'local'}")

        # Debug supplémentaire pour s'assurer que le bucket est correct
        if bucket == "":
            print("Warning: Bucket not defined. Predictions will be saved locally.")
        else:
            print(f"Using bucket: {bucket}")

        # 2. Load the dataset
        print("- Loading dataset")
        feat_data = "featurized_data"
        dataset_path = f"{bucket}{path}/{feat_data}.csv"

        if bucket == "":
            # Chemin local
            if not os.path.exists(dataset_path):
                raise FileNotFoundError(f"Dataset not found at {dataset_path}")
            df = pd.read_csv(dataset_path)
        else:
            # Chargement depuis S3
            s3 = boto3.client('s3')
            bucket_name = bucket.replace("s3://", "").split("/")[0]
            local_file = "featurized_data.csv"
            s3.download_file(bucket_name, f"{path}/{feat_data}.csv", local_file)
            df = pd.read_csv(local_file)
            print(f"Dataset downloaded from S3 bucket: {bucket_name}")

        target = 'specie'
        features = df.columns[:-1]
        y = df[target]
        X = df[features]

        # 3. Load trained model
        print("- Loading model")
        model_path = 'models/'
        run_model = ut.get_model(bucket=bucket, folder=model_path, model_name=name, use=model)

        if not run_model:
            raise ValueError("No valid model run ID found. Check the model name or 'latest' tag.")

        mlflow.set_tracking_uri("http://52.4.70.65:5000")  # URI de suivi MLflow
        full_model_path = f"{bucket}{model_path}{run_model}/artifacts/{name}/"

        try:
            if bucket == "":
                loaded_model = mlflow.pyfunc.load_model(f"{model_path}{run_model}/artifacts/{name}/")
            else:
                loaded_model = mlflow.pyfunc.load_model(full_model_path)
        except Exception as e:
            raise ValueError(f"Failed to load model from {full_model_path}: {e}")

        print("Model loaded successfully.")

        # 4. Perform prediction
        print("- Performing prediction")
        pred = loaded_model.predict(X)

        # 5. Evaluate model accuracy
        accuracy = accuracy_score(y, pred)
        print(f"Model Accuracy: {accuracy:.2f}")

        # 6. Append predictions to the dataset
        df[target] = pred

        # 7. Save dataset with predictions
        print("- Saving dataset with predictions")
        output_file = f"{bucket}{path}/prediction.csv"

        if bucket == "":
            # Local save
            df.to_csv(output_file, index=False)
            print(f"Predictions saved locally at: {output_file}")
        else:
            # Upload to S3
            local_file = "prediction.csv"
            df.to_csv(local_file, index=False)
            s3.upload_file(local_file, bucket_name, f"{path}/prediction.csv")
            print(f"Predictions uploaded to S3 bucket: {bucket_name}/{path}/prediction.csv")

        print("Predictions process completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_prediction()
