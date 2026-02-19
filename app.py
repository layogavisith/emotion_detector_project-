from flask import Flask, render_template, request
from emotion_detector import emotion_detector
import logging

app = Flask(__name__)

logging.basicConfig(filename="logs/app.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    text = request.form["text"]
    result = emotion_detector(text)

    if "error" in result:
        logging.error(result["error"])
        return render_template("index.html", error=result["error"])

    logging.info(f"Text analyzed: {text} → Emotion: {result['dominant_emotion']}")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)