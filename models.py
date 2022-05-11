# pylint: disable=C0114, C0115, C0116, E1101, R0903

from flask_login import UserMixin
from app import db


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    movie_title = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.String(2), nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __init__(self, movie_title, username, rating, comment):
        self.movie_title = movie_title
        self.username = username
        self.rating = rating
        self.comment = comment
