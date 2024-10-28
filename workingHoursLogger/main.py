from . import db
from .models import User, WorkingHours
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, current_user
from datetime import datetime

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
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@mainBp.route('/new')
@login_required
def new_working_hours():
    return render_template('create_working_hours.html')

@mainBp.route('/new', methods=['POST'])
@login_required
def new_working_hours_post():
    hours = request.form.get('hours')    
    comment = request.form.get('comment')
    pet_name = request.form.get('pet_name')
    date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()

    # create record in WorkingHours table
    workingHours = WorkingHours(hours=hours, date_posted=date, pet_name=pet_name, comment=comment, author=current_user )
    db.session.add(workingHours)
    db.session.commit()

    flash('Your hours has been added!')

    return redirect(url_for('main.user_working_hours'))


@mainBp.route('/all')
@login_required
def user_working_hours():
    user = User.query.filter_by(email=current_user.email).first_or_404()
    #hours = user.hours
    page = request.args.get('page', 1, type=int)
    hours = WorkingHours.query.filter_by(author=user).paginate(page = page, per_page=3)
    return render_template('all_hours.html', hours=hours, user=user)


@mainBp.route('/hour/<int:hour_id>/update', methods=['GET', 'POST'])
@login_required
def update_working_hours(hour_id):
    hour = WorkingHours.query.get_or_404(hour_id)

    if request.method == 'POST':
        
        #TODO: update only the fields that are filled in

        hour.hours = request.form['hours']
        hour.comment = request.form.get('comment')
        hour.pet_name = request.form.get('pet_name')
        hour.date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        db.session.commit()
        flash('Your working hours have been updated!')        
        return redirect(url_for('main.user_working_hours'))

    return render_template('update_working_hours.html', hour=hour)

@mainBp.route('/hour/<int:hour_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_working_hours(hour_id):
    hour = WorkingHours.query.get_or_404(hour_id)
    db.session.delete(hour)
    db.session.commit()
    flash('Your hours has been deleted!')

    return redirect(url_for('main.user_working_hours'))