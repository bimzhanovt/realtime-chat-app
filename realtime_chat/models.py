from realtime_chat import app
from realtime_chat.constants import *

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()
db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_NAME_LENGTH),
        index=True, unique=False, nullable=False)
    surname = db.Column(db.String(MAX_NAME_LENGTH),
        index=True, unique=False, nullable=False)
    username = db.Column(db.String(MAX_USERNAME_LENGTH),
        index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(PASSWORD_HASH_LENGTH),
        index=False, unique=False, nullable=False)

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
