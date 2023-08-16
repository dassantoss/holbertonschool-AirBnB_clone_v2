#!/usr/bin/python3
"""
This module defines a Flask application with specific routes and parameters.
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!' when accessing /.
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """
    Route that displays 'HBNB' when accessing /hbnb.
    """
    return 'HBNB'


@app.route('/c/<text>')
def display_c(text):
    """
    Route that displays 'C <text>' when accessing /c/<text>.
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
