#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_sess(close):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    obj_state = storage.all("State")
    obj_amenity = storage.all("")
    return render_template(
                "10-hbnb_filters.html",
                state=obj_state,
                amenity=obj_amenity
            )


if __name__ == "__main__":
    app.run()
