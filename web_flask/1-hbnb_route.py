#!/usr/bin/python3
"""
This module defines a basic Flask application with specific route /hbnb.
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
