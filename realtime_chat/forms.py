from realtime_chat.constants import *

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, EqualTo

class SignupForm(FlaskForm):
    name = StringField('First name', validators=NAME_VALIDATORS)
    surname = StringField('Last name', validators=NAME_VALIDATORS)
    username = StringField('Username', validators=USERNAME_VALIDATORS)
    password = PasswordField('Password',
        validators=[DataRequired(), EqualTo('confirm')])
    confirm = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=USERNAME_VALIDATORS)
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class LogoutForm(FlaskForm):
    submit = SubmitField('Log out')

class NewChatForm(FlaskForm):
    name = StringField('Chat name', validators=CHAT_NAME_VALIDATORS)
    submit = SubmitField('Create chat')

class AddChatMemberForm(FlaskForm):
    username = StringField('New member\'s username',
        validators=USERNAME_VALIDATORS)
    submit = SubmitField('Add new member')
