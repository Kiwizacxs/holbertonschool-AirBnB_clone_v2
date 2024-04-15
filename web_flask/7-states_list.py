#!/usr/bin/python3
""" module that start a flask app"""
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """this function close a session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_html():
    """this metod display a html"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
