from flask import Blueprint, render_template, jsonify
import requests
from flask import request

from rest.db import get_db

bp = Blueprint("home", __name__)

# utill functions


def get_to_do():
    """
    an utill function to show how to do http request
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    return jsonify(response.json())


# templating


@bp.route("/")
def index():
    return render_template("index.html")


# rest api


@bp.route("/todos")
def todos():
    return get_to_do()


@bp.route("/register", methods=("GET", "POST"))
def register():

    if request.method == "POST":
        # det dict
        user = request.get_json()
        print(user)

        db = get_db()

        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (user["username"], user["password"]),
        )
        db.commit()

        return jsonify({"success": True}), 200, {"ContentType": "application/json"}


@bp.route("/users")
def get_users():
    db = get_db()
    users = db.execute("SELECT * FROM user").fetchall()

    user_list = {"users": []}
    for user in users:
        user_list["users"].append(list(user))
    return jsonify(user_list)
