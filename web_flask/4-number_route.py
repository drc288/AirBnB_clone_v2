#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """ return the Hello HBNB!
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ return C plus the parameters
    """
    return "C {}".format(text.replace("_", " "))

@app.route('/python', defaults={'text': "is fun"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ return Python
    """
    return "Python {}".format(text.replace("_", " "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return the number
    """
    return "{} is a number".format(n)

app.run(host='0.0.0.0')
