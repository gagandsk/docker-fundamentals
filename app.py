import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Gagandeep",
        "lastname": "Dass",
        "socialMedia":
        [
            {"instagramUser": "gagandsk"},
            {"linkedin": "gagandeepdasskaur"},
            {"githubUser": "gagandsk"}
        ],
        "blog": "https://gagandeepdass.com/",
        "author": "Gagandeep Dass"
    }
    return json.dumps(value)