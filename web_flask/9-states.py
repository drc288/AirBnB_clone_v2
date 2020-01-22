#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, state
app = Flask(__name__)


@app.teardown_appcontext
def close_sess(close):
    storage.close()


@app.route('/states', strict_slashes=False)
def city_state():
    """Cities by states
    """
    objs = storage.all("State").values()
    return render_template(
                "7-states_list.html",
                states=objs
            )


@app.route('/states/<id>', strict_slashes=False)
def states_int(id):
    """state is id is equal to .
    """
    objs = storage.all("State").values()
    position = {}
    for data in objs:
        if data.id == id:
            position = data
            break
        else:
            position = None
    return render_template(
                "9-states.html",
                state=position
            )


if __name__ == "__main__":
    app.run()
