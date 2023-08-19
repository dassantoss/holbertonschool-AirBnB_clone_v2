#!/usr/bin/python3
"""Flask web application that returns an alternating html page"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    sl = storage.all(State)
    return render_template('7-states_list.html', sl=sl)


@app.teardown_appcontext
def closing_time(self):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
