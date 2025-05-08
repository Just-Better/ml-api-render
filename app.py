from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    return jsonify({"prediction": 1})  # przykładowa odpowiedź

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
