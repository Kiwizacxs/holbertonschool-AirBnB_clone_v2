#!/usr/bin/python3
""" module that start a flask app"""
from flask import Flask
from models import storage
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """this metod display a html"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exception):
    """this function close a session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
