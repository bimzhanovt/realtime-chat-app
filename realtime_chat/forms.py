from realtime_chat.constants import *

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, EqualTo

class SignupForm(FlaskForm):
    username = StringField('Username', validators=USERNAME_VALIDATORS)
    password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('confirm')])
    confirm = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=USERNAME_VALIDATORS)
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Log In')

class LogoutForm(FlaskForm):
    submit = SubmitField('Log out')
