from flask import Blueprint, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash
from .models import User
from . import db

authBp = Blueprint('auth', __name__)

@authBp.route('/signup')
def signup():
    return render_template('signup.html')


@authBp.route('/signup', methods=['POST'])
def signup_post():
    # get the info captured from the html form to server..
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # TODO: send to database

    # Query user table to get the first row matching email
    user = User.query.filter_by(email=email).first()
    
    if user:
        print('User already Exists!')
    
    else:
        print('Create new user')
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()

    return redirect(url_for('auth.login'))
    

@authBp.route('/login')
def login():
    return render_template('login.html')

@authBp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')    
    password = request.form.get('password')

    print(email, password)

    return redirect(url_for('main.profile'))


@authBp.route('/logout')
def logout():
    return "Page for users logout"


