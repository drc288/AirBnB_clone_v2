#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def close_sess(close):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_state():
    """Cities by states
    """
    objs = storage.all("State").values()
    return render_template(
                "8-cities_by_states.html",
                states=objs
            )


if __name__ == "__main__":
    app.run()
