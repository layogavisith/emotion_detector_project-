import json
import requests

API_URL = "https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/v1/analyze"
API_KEY = "YOUR_WATSON_API_KEY"

def emotion_detector(text):
    if not text.strip():
        return {"error": "Input text cannot be empty!"}

    try:
        response = requests.post(
            API_URL,
            auth=("apikey", API_KEY),
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "text": text,
                "features": {"emotion": {}}
            })
        )

        result = response.json()
        emotions = result["emotion"]["document"]["emotion"]

        dominant = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant
        }

    except Exception as e:
        return {"error": "API request failed", "details": str(e)}