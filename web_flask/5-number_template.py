#!/usr/bin/python3
"""
This module defines a Flask application with specific routes and parameters.
"""

from flask import Flask, render_template


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


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text='is cool'):
    """
    Route that displays 'Python <text>' when accessing
    /python or /python/<text>. Default value of text is 'is cool'.
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def display_number(n):
    """
    Route that displays '<n> is a number' when accessing /number/<n>.
    Only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def display_html(n):
    """
    Route that displays an HTML page with 'Number: n' in an H1 tag.
    Only if n is an integer.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
