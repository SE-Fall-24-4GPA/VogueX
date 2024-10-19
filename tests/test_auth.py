from flask import Flask, g
import json
from website.auth import auth
from website.auth import db
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sys

sys.path.append("..")


def test_login_get(app):
    client = app.test_client()
    url = "/login"

    response = client.get(url)
    print(response.get_data())
    assert response.status_code == 200


def test_login_post(app):
    client = app.test_client()
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    # This user is not present in the db
    data = {"email": "test@gmail.com",
            "password": "password123"}
    url = "/login"

    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 200


def test_signup_get(app):
    client = app.test_client()
    url = "/sign-up"
    response = client.get(url)
    assert response.status_code, 200


def test_signup_post(app):
    client = app.test_client()
    url = "/sign-up"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    # This user is not present in the db
    data = {
        "email": "test@gmail.com",
        "firstName": "test_user",
        "lastName": "test_end_name",
        "gender": "unknown",
        "phoneNumber": 99999999999,
        "password1": "password123",
        "password2": "password123",
        "age": 25,
        "city": "Raleigh",
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code, 200


def test_login_check_positive_case(app):
    client = app.test_client()
    url = "/login"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    data = {
        "email": "test@gmail.com",
        "password": "password123",
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code, 200
