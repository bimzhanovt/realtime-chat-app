from realtime_chat import app
from realtime_chat.models import *
from realtime_chat.forms import *
from realtime_chat.login import *
from realtime_chat.logging import *

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, \
    current_user

@app.route('/')
def home():
    logout_form = LogoutForm()
    return render_template('index.html', logout_form=logout_form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        try:
            user = User(username, signup_form.password.data)
            db.session.add(user)
            db.session.commit()
            log_user_signup(username)
            login_user(user, remember=True)
            log_user_login(username)
            return redirect(url_for('home'))
        except ValueError:
            log_user_unsuccessful_sign_up(username)
            flash('There already exists a user with the same username')
    return render_template('signup.html', signup_form=signup_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(login_form.password.data):
            login_user(user, remember=login_form.remember.data)
            log_user_login(username)
            return redirect(url_for('home'))
        else:
            flash('The username or password you entered is incorrect')
            log_user_unsuccessful_log_in(username)
    return render_template('login.html', login_form=login_form)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    username = current_user.username
    logout_user()
    log_user_logout(username)
    return redirect(url_for('home'))
