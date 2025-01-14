from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)