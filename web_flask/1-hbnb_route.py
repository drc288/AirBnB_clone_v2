#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def app_01():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def app_02():
    return "HBNB"

app.run()
