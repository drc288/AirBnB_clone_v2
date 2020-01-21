#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web_flask():
    """create a basic page
    """
    return "Hello HBNB!"


app.run(host="0.0.0.0")
