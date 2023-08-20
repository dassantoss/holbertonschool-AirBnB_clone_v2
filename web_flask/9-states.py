#!/usr/bin/python3
"""
Script that starts a Flask application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    """Displays a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_db(self):
    """
    Close the current SQLAlchemy session after each request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)