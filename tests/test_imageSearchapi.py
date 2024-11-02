# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from urllib import response
from flask import Flask, g
import json
from website.auth import auth
from website.auth import db
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sys
from website.models import User

sys.path.append("..")


# running
def test_recommendations(app):
    client = app.test_client()

    data = json.dumps({"occasion": "birthday", "city": "Raleigh"})
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype
        # 'Accept': mimetype
    }

    url = "/recommendations"
    with client as c:
        var = c.post(url, data=data, headers=headers)
        assert var.status_code == 403


#### [WIP] trying to mock DB
def test_recommendations_with_session(app):
    client = app.test_client()

    data = json.dumps({"occasion": "birthday", "city": "Raleigh"})
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype
        # 'Accept': mimetype
    }

    url = "/recommendations"
    with client as c:
        with c.session_transaction() as sess:
            sess["userid"] = 1

        var = c.post(url, data=data, headers=headers)
        assert var.status_code == 200
