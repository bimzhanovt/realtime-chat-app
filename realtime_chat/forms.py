from realtime_chat.constants import *

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Regexp

class SignupForm(FlaskForm):
    username = StringField('Username',
        validators=[
            Length(min=MIN_USERNAME_LENGTH, max=MAX_USERNAME_LENGTH),
            Regexp(USERNAME_REGEXP, message=USERNAME_REGEXP_MESSAGE),
        ],
    )
    password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('confirm')])
    confirm = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Log In')

class LogoutForm(FlaskForm):
    submit = SubmitField('Log out')
