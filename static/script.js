const video = document.getElementById('video');

// Start Camera
navigator.mediaDevices.getUserMedia({ video: true })
.then(stream => {
    video.srcObject = stream;
})
.catch(err => {
    alert("Camera not working");
});

function captureImage() {

    const emotions = ["happy", "sad", "angry"];
    const randomEmotion =
        emotions[Math.floor(Math.random() * emotions.length)];

    fetch("/predict", {
        method: "POST",
        body: new URLSearchParams({ mood: randomEmotion })
    })
    .then(res => res.json())
    .then(data => {

        document.getElementById("emotionText").innerText =
            `Emotion: ${data.emotion} (${data.confidence}%)`;

        let songsDiv = document.getElementById("songs");
        songsDiv.innerHTML = "";

        data.songs.forEach(song => {

            songsDiv.innerHTML += `
                <div class="song-card">
                    <img src="${song.image}" 
                    style="width:100%;border-radius:10px">

                    <h3>${song.name}</h3>
                    <p>${song.artist}</p>

                    <a href="${song.url}" target="_blank">
                    ▶ Play on YouTube
                    </a>
                </div>
            `;
        });

    });
}