import imp
import os
import tempfile
import pytest
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
import sys

sys.path.append("..")

#from website.auth import db

#db = SQLAlchemy()


with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://fashion:fashion@localhost/fashion_test'

    import website.views
    import website.auth

    import website.preferences
    import website.recommendations

    app.register_blueprint(website.views.views, url_prefix="/")
    app.register_blueprint(website.auth.auth, url_prefix="/")
    app.register_blueprint(website.preferences.preferencesbp)
    app.register_blueprint(website.recommendations.recommendationsbp)
    return app



@pytest.fixture
def app():
    #db_fd, db_path = tempfile.mkstemp()
    from website import create_app

    app = create_app(
        test_config={
            "SECRET_KEY": "hjshjhdjah kjshkjdhjs",
            "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://fashion:fashion@localhost/fashion_test"
        }
    )
    yield app

    #os.close(db_fd)
    #os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
