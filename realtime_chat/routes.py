from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from realtime_chat import app
from realtime_chat.forms import *
from realtime_chat.logging import *
from realtime_chat.login import *
from realtime_chat.models import *


@app.route('/')
def home():
    logout_form = LogoutForm()
    new_chat_form = NewChatForm()
    if current_user.is_authenticated:
        chats=[Chat.query.get(chat.chat_id) for chat in current_user.chats]
        return render_template('index.html',
            logout_form=logout_form, new_chat_form=new_chat_form, chats=chats)
    else:
        return render_template('index.html',
            logout_form=logout_form, new_chat_form=new_chat_form)

@app.route('/chat/new', methods=['POST'])
@login_required
def new_chat():
    new_chat_form = NewChatForm()
    if new_chat_form.validate_on_submit():
        chat = Chat(new_chat_form.name.data, current_user.id)
    return redirect(url_for('chat', id=chat.id))

@app.route('/chat/<int:id>')
@login_required
def chat(id):
    logout_form = LogoutForm()
    add_chat_member_form = AddChatMemberForm()

    chat = Chat.query.get(id)
    is_chat_member = ChatMember.query.filter_by(chat_id=chat.id,
        user_id=current_user.id).first()

    if chat:
        if is_chat_member:
            return render_template('chat.html',
                logout_form=logout_form,
                add_chat_member_form=add_chat_member_form,
                chat=chat,
                messages=[{'username': User.query.get(message.user_id).username,
                        'text': message.text,
                        'time': message.time.strftime("%H:%M"),
                    } for message in chat.messages
                ]
            )
        else:
            flash('You are not a member of this chat')
    else:
        flash('The chat you are trying to access does not exist')
    return redirect(url_for('home'))

@app.route('/chat/<int:chat_id>/member/add', methods=['POST'])
@login_required
def add_chat_member(chat_id):
    form = AddChatMemberForm()

    if not Chat.query.get(chat_id):
        flash('This chat does not exist')
        return redirect(url_for('home'))

    if form.validate_on_submit():
        username = username=form.username.data

        try:
            user = User.query.filter_by(username=username).first()
            if not user:
                raise ValueError('This user does not exist')

            chat_member = ChatMember(chat_id, user.id)
            flash(f'{username} has been successfully added')
        except ValueError as error:
            flash(str(error))
    return redirect(url_for('chat', id=chat_id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        username = signup_form.username.data
        try:
            user = User(username,
                signup_form.name.data, signup_form.surname.data,
                signup_form.password.data)
            log_user_action(LOG_MESSAGES['user_signup'], username)
            login_user(user, remember=False)
            log_user_action(LOG_MESSAGES['user_login'], username)
            return redirect(url_for('home'))
        except ValueError as error:
            log_user_action(LOG_MESSAGES['user_unsuccessful_signup'], username)
            flash(str(error))
    return render_template('signup.html', signup_form=signup_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(login_form.password.data):
            login_user(user, remember=False)
            log_user_action(LOG_MESSAGES['user_login'], username)
            return redirect(url_for('home'))
        else:
            log_user_action(LOG_MESSAGES['user_unsuccessful_login'], username)
            flash('The username or password you entered is incorrect')
    return render_template('login.html', login_form=login_form)

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    username = current_user.username
    logout_user()
    log_user_action(LOG_MESSAGES['user_logout'], username)
    return redirect(url_for('home'))
