# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from . import db
from flask_login import UserMixin
from .CustomMixin import SerializerMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    gender = db.Column(db.String(20))
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(150))
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))


class Preference(db.Model, UserMixin):
    userid = db.Column(db.Integer, primary_key=True)
    preferences = db.Column(db.Text)


class Favourite(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    favourite_url = db.Column(db.String(255))
    search_occasion = db.Column(db.String(255))
    search_weather = db.Column(db.String(255))
