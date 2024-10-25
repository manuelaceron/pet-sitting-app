from . import db
from flask_login import UserMixin

#db.Model: This is the base class for all SQLAlchemy models. It allows the User class to be mapped to a database table, with each instance representing a record in that table
#UserMixin allow to work witj user sessions, and authentication in flaks applications

#User class represent User table in model

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique =True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

