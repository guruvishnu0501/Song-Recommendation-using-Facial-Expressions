from flask import Flask, request, jsonify, render_template
import requests
import random

app = Flask(__name__)

# 🔑 Put your YouTube API Key
YOUTUBE_API_KEY = "****"


# =========================
# Home
# =========================
@app.route('/')
def home():
    return render_template("index.html")


# =========================
# Predict
# =========================
@app.route('/predict', methods=['POST'])
def predict():

    mood = request.form.get("mood")

    if not mood:
        mood = "happy"

    confidence = round(random.uniform(80, 99), 2)

    query = f"{mood} songs"

    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 5,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    songs = []

    for item in data["items"]:
        songs.append({
            "name": item["snippet"]["title"],
            "artist": item["snippet"]["channelTitle"],
            "image": item["snippet"]["thumbnails"]["high"]["url"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })

    return jsonify({
        "emotion": mood,
        "confidence": confidence,
        "songs": songs
    })


if __name__ == '__main__':
    app.run(debug=True)
