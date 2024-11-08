from .app import db
from flask_login import UserMixin
from datetime import datetime

#db.Model: This is the base class for all SQLAlchemy models. It allows the User class to be mapped to a database table, with each instance representing a record in that table
#UserMixin allow to work witj user sessions, and authentication in flaks applications

#User class represent User table in model

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique =True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    # TODO: Why?
    hours = db.relationship('WorkingHours', backref='author', lazy=True)
    pets = db.relationship('Pet', backref='owner', lazy=True)

class WorkingHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hours = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)    
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pet_id = db.Column(db.Integer,db.ForeignKey('pet.id'), nullable=False)

    pet = db.relationship('Pet', backref='working_hours', lazy=True)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    sitter = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    

    