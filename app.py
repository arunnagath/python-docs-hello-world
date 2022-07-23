from flask import Flask
from PIL import Image
import requests
from io import BytesIO

response = requests.get(https://st2.depositphotos.com/1000393/11789/i/950/depositphotos_117893952-stock-photo-hacker-with-mask.jpg)
img = Image.open(BytesIO(response.content))
app = Flask(__name__)

@app.route("/")
def hello():
    return "ZEE Hacked by Appsec Team"
