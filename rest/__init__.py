import os
import os
from flask import Flask


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # add db config

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(PROJECT_ROOT, "rest.sqlite"),
    )

    # register the database commands

    from rest import db

    db.init_app(app)

    # add application to project

    from rest import Home

    app.register_blueprint(Home.bp)

    app.add_url_rule("/", endpoint="index")

    return app
