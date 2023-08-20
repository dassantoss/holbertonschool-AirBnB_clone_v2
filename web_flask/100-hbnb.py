#!/usr/bin/python3
"""
Script that starts a Flask application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hbnb_filters():
    """Displays a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(self):
    """
    Close the current SQLAlchemy session after each request
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
