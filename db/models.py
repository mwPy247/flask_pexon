""" The module defines all sql models to be used by the database. """
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Database Models
class Movie(db.Model):
    """ Provides a blueprint for the creation of the 'movies' table. """
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    director = db.Column(db.String)
    language = db.Column(db.String)
    title = db.Column(db.String)
