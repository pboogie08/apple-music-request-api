from flask import Flask, request
import requests
import urllib.parse

app = Flask(__name__)

@app.route("/")
def home():
    return "Apple Music Request API is running."

@app.route("/search")
def search_song():
    query = request.args.get("query")
    if not query:
        return "No song provided."

    encoded_query = urllib.parse.quote(query)
    url = f"https://itunes.apple.com/search?term={encoded_query}&entity=song&limit=1"
    response = requests.get(url)
    data = response.json()

    if data["resultCount"] == 0:
        return "Song not found."

    track = data["results"][0]
    track_id = track["trackId"]
    track_name = track["trackName"]
    artist = track["artistName"]

    apple_link = f"https://music.apple.com/us/song/id{track_id}"
    return f"{track_name} - {artist} | {apple_link}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
