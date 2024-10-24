from flask import Blueprint, render_template, url_for, request, redirect

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

    print(email, name, password)

    # TODO: send to database

    return redirect(url_for('auth.login'))
    

@authBp.route('/login')
def login():
    return render_template('login.html')

@authBp.route('/logout')
def logout():
    return "Page for users logout"


