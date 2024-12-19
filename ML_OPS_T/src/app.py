from flask import Flask, request, jsonify
from src.models.predict import predict
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenue sur l'API de prédiction du modèle ML !"

@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        # Récupère les données en JSON
        data = request.get_json()
        features = data["features"]
        
        # Appelle la fonction de prédiction
        prediction = predict(features)
        
        # Retourne la prédiction en JSON
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
