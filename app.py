from flask import Flask
from PIL import Image
im=image.open("https://st2.depositphotos.com/2501025/5654/i/450/depositphotos_56545139-stock-photo-password.jpg")
im.show()
app = Flask(__name__)

@app.route("/")
def hello():
    return "ZEE Hacked by Appsec Team"
