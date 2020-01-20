#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def app_01():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def app_02():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def app_03(text):
    return "C {}".format(text.replace("_", " "))

app.run()
