from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from realtime_chat import app
from realtime_chat.constants import *

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH), index=True, nullable=False)
    surname = db.Column(db.String(MAX_NAME_LENGTH), index=True, nullable=False)
    username = db.Column(db.String(MAX_USERNAME_LENGTH),
        index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(PASSWORD_HASH_LENGTH), nullable=False)

    chats = db.relationship('ChatMember', backref='user', lazy='dynamic')
    messages = db.relationship('ChatMessage', backref='user', lazy='dynamic')

    def __init__(self, username, name, surname, password):
        if User.query.filter_by(username=username).first():
            raise ValueError(
                'There already exists a user with the same username')
        else:
            super().__init__(username=username, name=name, surname=surname,
                password_hash=generate_password_hash(password))
            try:
                db.session.add(self)
                db.session.commit()
            except:
                db.session.rollback()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(cls, password):
        return check_password_hash(cls.password_hash, password)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_CHAT_NAME_LENGTH),
        index=True, nullable=False)

    members = db.relationship('ChatMember', backref='chat', lazy='dynamic',
        cascade = 'all, delete, delete-orphan')
    messages = db.relationship('ChatMessage', backref='chat', lazy='dynamic',
        cascade = 'all, delete, delete-orphan')

    def __init__(self, name, creator_id):
        super().__init__(name=name)
        db.session.add(self)

        first_member = ChatMember(chat_id=self.id, user_id=creator_id)
        self.members.append(first_member)

        try:
            db.session.commit()
        except:
            db.session.rollback()

class ChatMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, chat_id, user_id):
        if ChatMember.query.filter_by(chat_id=chat_id, user_id=user_id).first():
            raise ValueError('This user is already in the chat')

        super().__init__(chat_id=chat_id, user_id=user_id)

        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String(MAX_MESSAGE_TEXT_LENGTH), nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, chat_id, user_id, text):
        super().__init__(chat_id=chat_id, user_id=user_id, text=text)
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
