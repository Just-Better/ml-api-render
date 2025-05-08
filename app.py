from flask import Flask, request, jsonify
import numpy as np
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Przygotowanie modelu ML (iris + RandomForest)
data = load_iris()
clf = RandomForestClassifier()
clf.fit(data.data, data.target)

# Endpoint: /predict
@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.json["input"]
        prediction = clf.predict([input_data])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint: /config — odczyt zmiennej środowiskowej
@app.route("/config", methods=["GET"])
def config():
    message = os.getenv("APP_MESSAGE", "Brak wiadomości")
    return jsonify({"message": message})

# Uruchomienie aplikacji
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
