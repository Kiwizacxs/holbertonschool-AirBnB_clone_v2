#!/usr/bin/python3
"""
module that contain apps
"""
from flask import Flask
from markupsafe import escape as escape
from flask import render_template
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


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def only_number(n):
    return f"{escape(int(n))} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, ooe="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, ooe="odd")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
