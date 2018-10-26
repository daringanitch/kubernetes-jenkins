import os, math
from flask import Flask, request, render_template
from datetime import datetime
import requests

app = Flask(__name__)



@app.route('/')
def index():
    return 'Jenkins test', 200

@app.route('/sentence')
def sentence():
    return 'Hello World, Jenkins version 333333', 200

@app.route('/hello')
def hello():
    return 'Hello World, Jenkins version: %s' % (datetime.now())






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
