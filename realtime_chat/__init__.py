import secrets
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=secrets.token_hex(16),
    SQLALCHEMY_DATABASE_URI='sqlite:///realtime_chat.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

import realtime_chat.routes
