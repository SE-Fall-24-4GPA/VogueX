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
    ratings = db.Column(db.Integer)
    review = db.Column(db.String(500))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Assuming you have a User model
    favourite_url = db.Column(db.String(255), nullable=False)  # Ensure this matches the Favourite URL
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    @staticmethod
    def serialize(review):
        return {
            "id": review.id,
            "userid": review.userid,
            "favourite_url": review.favourite_url,
            "rating": review.rating,
            "comment": review.comment
        }