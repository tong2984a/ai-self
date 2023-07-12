import os
import requests
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))
api_key = os.getenv("API_KEY")
print(api_key)

#setting up the talk

# copied url from response in audios.py 
audio_url = "s3://d-id-audios-prod/auth0|64ae01bbee6719d9da99dc7c/ORCOje7ARqYOa_bhu03Pg/sample-3.wav"

url = "https://api.d-id.com/talks"
payload = {
    "script": {
        "type": "audio",
        "subtitles": "false",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-JennyNeural"
        },
        "ssml": "false",
        "reduce_noise": "false",
        "audio_url": audio_url
    },
    "config": {
        "fluent": "false",
        "pad_audio": "0.0"
    },
    "source_url": "https://as2.ftcdn.net/v2/jpg/01/28/41/29/1000_F_128412995_e1rdKIAIlxKunn7a7PSAhDp0K1s4g3EB.jpg",
    "webhook": "http://3046.chickenkiller.com:8300/webhook"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic " + api_key
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

