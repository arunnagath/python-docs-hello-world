from flask import Flask
app = Flask(__name__)
import urllib

@app.route("/")

def hello():
    return urllib.urlopen('https://thumbs.dreamstime.com/z/hacker-picture-computer-44924818.jpg')

