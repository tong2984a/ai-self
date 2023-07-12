import os
import requests
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))
api_key = os.getenv("API_KEY")
print(api_key)

#setting up audio
url = "https://api.d-id.com/audios"

files = { "audio": ("sample-3.mp3", open("sample-3.mp3", "rb"), "audio/mpeg") }
headers = {
    "accept": "application/json",
    "authorization": "Basic " + api_key
}

response = requests.post(url, files=files, headers=headers)

print(response.text)
#print(response.text)
#get the audio url from the response object
audio_url = response.json()["url"]
print(audio_url)

