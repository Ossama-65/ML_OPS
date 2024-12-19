import numpy as np
import pandas as pd
import random
import string
import os
import boto3
import s3fs
from datetime import datetime
from pyathena import connect
from pyathena.pandas.cursor import PandasCursor
import sklearn.metrics as metrics

F1_THRESHOLD = 0.8

def get_bucket_from_env(environment):
    """
    Return S3 bucket path based on the environment.
    """
    if environment != 'local':
        return f"s3://mlops-prod-bucket-ok/"
    raise ValueError("Environment must be 'prod' or 'dev'. Local not allowed.")

def get_pyathena_connector(bucket, region, pd_cursor=False):
    """
    Connect to AWS Athena using PyAthena.
    """
    conn = connect(
        s3_staging_dir=bucket,
        region_name=region,
        cursor_class=PandasCursor if pd_cursor else None
    )
    return conn.cursor() if pd_cursor else conn

def get_df_from_query(file, conn, cursor=False):
    """
    Run SQL query from file and return DataFrame.
    """
    with open(file, 'r') as query_file:
        query = query_file.read()
    if cursor:
        df = conn.execute(query).as_pandas()
    else:
        df = pd.read_sql(query, conn)
    return df

def create_data_version_control(df, bucket, name="data"):
    """
    Save DataFrame to S3 with version control.
    """
    dvc_file_name = f"{name}_{gen_dataset_dvc(8)}.csv"
    local_path = f"/tmp/{dvc_file_name}"
    s3_path = f"{bucket}data/{dvc_file_name}"

    df.to_csv(local_path, index=False)
    s3 = boto3.client('s3')
    bucket_name = bucket.replace("s3://", "").split("/")[0]
    s3.upload_file(local_path, bucket_name, f"data/{dvc_file_name}")
    print(f"Dataset uploaded to: {s3_path}")
    return s3_path

def eval_classification_metrics(real, pred):
    """
    Evaluate classification model metrics.
    """
    report = metrics.classification_report(real, pred)
    accuracy = metrics.accuracy_score(real, pred)
    f1 = metrics.f1_score(real, pred, average='micro')
    precision = metrics.precision_score(real, pred, average='micro')
    recall = metrics.recall_score(real, pred, average='micro')
    conf_mat = metrics.confusion_matrix(real, pred)
    return report, accuracy, f1, precision, recall, conf_mat

def is_classification_model_approved(f1):
    """
    Check if model's F1 score meets the approval threshold.
    """
    return f1 > F1_THRESHOLD

def deploy_model(bucket, run, location):
    """
    Deploy model to S3 bucket.
    """
    folder = f"mlruns/0/{run}/"
    s3_fs = s3fs.S3FileSystem()
    s3_path = f"{bucket}{location}"
    print(f"Deploying model to: {s3_path}")
    s3_fs.put(folder, s3_path, recursive=True)

def get_model(bucket, folder, model_name, use='latest'):
    """
    Get the model path from S3.
    """
    s3 = boto3.client('s3')
    bucket_name = bucket.replace("s3://", "").split("/")[0]

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder)
    models = [obj['Key'].split('/')[-2] for obj in response.get('Contents', []) if model_name in obj['Key']]

    print(f"- Model requested: {use}")
    print("- Models found:", models)

    if not models:
        raise ValueError("No models found in the specified folder.")
    
    models = sorted(models, reverse=True)
    if use == 'latest':
        return models[0]
    else:
        filtered = [m for m in models if use in m]
        return filtered[0] if filtered else None

def gen_dataset_dvc(length=8):
    """
    Generate versioned dataset name.
    """
    return f'{get_current_date()}_{get_random_string(length)}'

def get_current_date():
    """
    Get current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def get_random_string(length=8, str_list=string.ascii_letters):
    """
    Generate random string.
    """
    return ''.join(random.choice(str_list) for _ in range(length))
