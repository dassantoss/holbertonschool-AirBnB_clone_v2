#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
    Display a HTML page with a list of all State objects present
    in DBStorage
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """
    Close the current SQLAlchemy session after each request
    """
    storage.close()


if __name__ == ('_main__'):
    app.run(host='0.0.0.0', port=5000)
