import os
import requests
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))
api_key = os.getenv("API_KEY")
print(api_key)

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic " + api_key
}

id = "tlk_8O7BFppTvFJCAGqR7XPhp"
url2 = "https://api.d-id.com/talks/" + id
response2 = requests.get(url2, headers=headers)
print(response2.text)

image ="https://d-id-talks-prod.s3.us-west-2.amazonaws.com/google-oauth2%7C117330314217329163437/tlk_8O7BFppTvFJCAGqR7XPhp/1689118429946.mp4?AWSAccessKeyId=AKIA5CUMPJBIK65W6FGA&Expires=1689204832&Signature=qKz0bmu3ouA599F1nDWnvVRJK9Y%3D&X-Amzn-Trace-Id=Root%3D1-64ade6e0-34b42b904dc601c47668658f%3BParent%3Db7e5ea2414ca494d%3BSampled%3D1%3BLineage%3D6b931dd4%3A0"
