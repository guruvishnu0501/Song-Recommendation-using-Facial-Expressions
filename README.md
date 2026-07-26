# 🎵 Emotion Music Recommender using Facial Expressions

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-green.svg" />
  <img src="https://img.shields.io/badge/YouTube-Data%20API-red.svg" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
</p>

<p align="center">
  <b>Detect emotions and recommend songs instantly based on facial expressions.</b>
</p>

---

## 📖 Overview

**Emotion Music Recommender** is a Flask-based web application that recommends songs according to a user's detected facial emotion.

The application accesses the user's webcam, simulates facial emotion recognition (currently using demo/random inference), and fetches mood-specific songs from the **YouTube Data API v3**.

This project demonstrates the integration of:

- 🎥 Webcam Capture
- 😊 Emotion Recognition Workflow
- 🎵 Music Recommendation
- 🌐 Flask Backend
- 📺 YouTube Data API

The project is intentionally lightweight, making it an excellent starting point for integrating real AI-based facial emotion recognition.

---

# ✨ Features

- 📸 Webcam Access using JavaScript
- 😀 Simulated Facial Emotion Detection
- 🎵 Mood-Based Music Recommendations
- 📺 YouTube API Integration
- 🖥 Responsive User Interface
- ⚡ Fast Flask Backend
- 🔗 Direct YouTube Video Links
- 🧩 Easy to Extend with AI Models

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| JavaScript | Webcam & Client Logic |
| Requests | API Calls |
| YouTube Data API v3 | Song Search |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```
Song-Recommendation-using-Facial-Expressions/
│
├── static/
│   ├── script.js
│   ├── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

# 🚀 Application Workflow

```text
             User Opens Website
                     │
                     ▼
          Browser Requests Camera
                     │
                     ▼
       Capture Webcam Frame (JS)
                     │
                     ▼
       Detect Emotion (Demo Version)
                     │
                     ▼
      Send Emotion → Flask Backend
                     │
                     ▼
     YouTube Data API Search Request
                     │
                     ▼
      Receive Matching Song Results
                     │
                     ▼
     Display Songs with Thumbnails
```

---

# 📸 Screenshots



## Home Page

```
<img width="1918" height="977" alt="Screenshot 2026-07-27 000337" src="https://github.com/user-attachments/assets/901b1ac8-9f58-4869-842f-5d1e01667b41" />

```

## Webcam Detection

```
<img width="1913" height="972" alt="image" src="https://github.com/user-attachments/assets/4304e005-d6e3-422d-b7c4-81dacc0be48d" />

```

## Song Recommendations

```
<img width="1918" height="962" alt="image" src="https://github.com/user-attachments/assets/b2110b3c-e1c3-4fe4-98c7-c9726bd09282" />

```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/guruvishnu0501/Song-Recommendation-using-Facial-Expressions.git

cd Song-Recommendation-using-Facial-Expressions
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask requests python-dotenv
```

---

## 4️⃣ Configure API Key

Create a file named

```
.env
```

Add your YouTube API key

```env
YOUTUBE_API_KEY=YOUR_API_KEY
```

Then update **app.py**

```python
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
```

---

## 5️⃣ Run the Project

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 📡 API Documentation

## POST `/predict`

Returns song recommendations based on emotion.

### Request

```text
Form Data

mood = happy
```

Possible values

- happy
- sad
- angry

---

### Sample Response

```json
{
    "emotion": "happy",
    "confidence": 94.82,
    "songs": [
        {
            "name": "Happy Song",
            "artist": "Artist Name",
            "image": "...",
            "url": "https://youtube.com/..."
        }
    ]
}
```

---

# 🧠 Current Implementation

The current version uses a **random emotion generator** inside

```
static/script.js
```

This demonstrates the complete recommendation pipeline without requiring a trained AI model.

---

# 🚀 Future Enhancements

### 🤖 AI Emotion Recognition

Replace the random selection with

- Face API.js
- TensorFlow.js
- MediaPipe
- FER-2013 Model
- OpenCV

---

### 🎵 Better Recommendation Engine

- Spotify API
- Last.fm API
- Mood Classification
- Personalized Recommendations

---

### ☁ Deployment

Deploy using

- Render
- Railway
- Vercel
- Heroku
- AWS
- Azure

---

### 🔐 Security

- Environment Variables
- Secret Manager
- Rate Limiting
- Input Validation

---

### ⚡ Performance

- Redis Cache
- API Response Caching
- Lazy Loading
- CDN Support

---

### 📱 UI Improvements

- Dark Mode
- Loading Animations
- Better Cards
- Music Player
- Responsive Mobile UI

---

# 📊 Project Architecture

```text
             User
               │
               ▼
        HTML / CSS / JS
               │
               ▼
      Emotion Detection Logic
               │
               ▼
         Flask Backend
               │
               ▼
      YouTube Data API v3
               │
               ▼
      Recommended Songs JSON
               │
               ▼
         Browser Interface
```

---

# 🧪 Possible AI Upgrade

Replace the current demo logic with

```
Webcam

↓

Face Detection

↓

Emotion Recognition Model

↓

Predicted Emotion

↓

Recommendation Engine

↓

Songs
```

Possible models:

- FER-2013
- DeepFace
- MediaPipe
- TensorFlow CNN
- Face API.js

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes

```bash
git commit -m "Added New Feature"
```

4. Push

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

# 📋 TODO

- [ ] Real Emotion Detection
- [ ] Spotify Integration
- [ ] User Login
- [ ] Playlist Generation
- [ ] Music History
- [ ] Favorite Songs
- [ ] Docker Support
- [ ] CI/CD Pipeline
- [ ] Unit Tests
- [ ] Deployment

---

# 👨‍💻 Author

**Guru Vishnu**

Final Year B.Tech (CSE - IoT)

📧 Email: *your-email@example.com*

🌐 GitHub

https://github.com/guruvishnu0501

---

# 🌟 Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

🐛 Report Issues

💡 Suggest Improvements

---

# 📜 License

This project is licensed under the terms of the **MIT License**.

See the **LICENSE** file for more information.

---

# 🙏 Acknowledgements

- Flask
- Python
- YouTube Data API v3
- HTML5
- CSS3
- JavaScript
- Open Source Community

---

<p align="center">

⭐ If you like this project, don't forget to give it a star! ⭐

Made with ❤️ by Guru Vishnu

</p>
