#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def app_01():
    """create a basic page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def app_02():
    """create a secound page
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
