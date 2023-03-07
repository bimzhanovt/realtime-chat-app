from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import *

from realtime_chat.constants import *

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

class NewChatMemberForm(FlaskForm):
    username = StringField('New member\'s username',
        validators=USERNAME_VALIDATORS)
    submit = SubmitField('Add new member')
