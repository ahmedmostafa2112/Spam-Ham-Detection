import joblib
from flask import Flask, request, jsonify

model = joblib.load(r"E:\\Studying\\Spam detection\\spam_detection.pkl")
vectorizer = joblib.load(r"E:\\Studying\\Spam detection\\BoW_vectorizer.pkl")

app = Flask(__name__)

@app.route("/spamcheck", methods=["POST"])
def predict():

    data = request.get_json()
    message = data.get("m")

    if not message:
        return jsonify({"error": "Please provide a message"}), 400

    msg_vec = vectorizer.transform([message])

    prediction = model.predict(msg_vec)

    if prediction == 0:
        result = "ham"
    else:
        result = "spam"

    return jsonify({
        "message": message,
        "prediction": result
    })


if __name__ == "__main__":
    app.run()