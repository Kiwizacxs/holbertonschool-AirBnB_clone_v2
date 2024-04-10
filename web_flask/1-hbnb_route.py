#!/usr/bin/python3
"""
module taht start Flask web applcation
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    This method display an string
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def only_hbnb():
    """
    This method display an string
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
