from flask import Blueprint, render_template, request, flash, redirect, url_for
from . models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password, please try again", category='error')
        else:
            flash("Email does not exist", category='error')


    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_email = User.query.filter_by(email=email).first()
        user_username = User.query.filter_by(username=username).first()
        if user_email:
            flash("Email already exists.", category='error')
        elif user_username:
            flash("Username already exists.", category='error')
        elif len(email) < 8 and len(email) < 50:
            flash("Email not valid.", category='error')
        elif len(username) < 2 and len(username) < 50:
            flash("Username not valid.", category='error')
        elif password1 != password2:
            flash("Passwords do not match.", category='error')
        elif len(password1) < 8:
            flash("Password too short.", category='error')
        elif len(password1) > 100:
            flash("Password too long.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully.", category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)

    