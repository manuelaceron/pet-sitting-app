from flask import Blueprint, render_template

authBp = Blueprint('auth', __name__)

@authBp.route('/signup')
def signup():
    return render_template('signup.html')

@authBp.route('/login')
def login():
    return render_template('login.html')

@authBp.route('/logout')
def logout():
    return "Page for users logout"


