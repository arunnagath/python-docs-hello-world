from flask import Flask
app = Flask(__name__)
import urllib

fun open():
    return urllib.urlopen('https://thumbs.dreamstime.com/z/hacker-picture-computer-44924818.jpg')

@app.route("/")
def hello():
    return "Hacked by ZEE Appsec Team"
