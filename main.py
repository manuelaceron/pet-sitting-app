from flask import Blueprint, render_template, url_for


"""""
Blueprint: way to organize files in flask project
Split different functionalities into separate modules
Factor application into a set of Blueprints
Reuse different Blueprints for different applications
Related routs under common URL prefix

Blueprints are registered to the application
"""

mainBp = Blueprint('main', __name__)

@mainBp.route('/') #route home
def index():
    return render_template('index.html')

@mainBp.route('/profile')
def profile():
    return render_template('profile.html')