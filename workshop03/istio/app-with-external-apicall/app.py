#!/usr/bin/python

import os, math
from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

PORT = 6000

@app.route("/")
def main():
    return "Hellworld istio demo"

@app.route("/topstories")
def topStories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    resp_data = requests.get(url, headers = header)
    if resp_data.ok:
        resp_json = resp_data.json()
    else:
        resp_json = { "blocked": "true" }

    resp_data = json.dumps(resp_json)
    return Response(resp_data , 200, content_type="application/json")

@app.route('/hello')
def hello():
    version = os.environ.get('SERVICE_VERSION')

    # do some cpu intensive computation
    x = 0.0001
    for i in range(0, 1000000):
	    x = x + math.sqrt(x)

    return 'Hello version: %s, instance: %s\n' % (version, os.environ.get('HOSTNAME'))

@app.route('/health')
def health():
    return 'Helloworld is healthy', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
