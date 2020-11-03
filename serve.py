"""
@Author Chanwoo Gwon, Yonsei Univ. Researcher since 2020.05~
@Date 2020.11.03
"""
from flask import Flask, jsonify, request
from config import configure

import os

app = Flask(__name__)

version = "0.1"


@app.route("/")
def hello():
    return "Hello World"


@app.route("/cdm/ai/start", methods=['POST'])
def start():

    return jsonify({
        "id": "Not Implements start",
        "version": version,
        "result": "success"
    })


@app.route("/cdm/ai/init", methods=['POST'])
def init():

    return jsonify({
        "id": "Not Implements init",
        "version": version,
        "result": "success"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=configure["port"])
