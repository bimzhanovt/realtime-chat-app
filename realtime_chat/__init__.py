import secrets

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path='')
app.config.from_mapping(
    SECRET_KEY=secrets.token_hex(16),
    SQLALCHEMY_DATABASE_URI='sqlite:///realtime_chat.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
socketio = SocketIO(app)

import realtime_chat.chat
import realtime_chat.routes

if __name__ == '__main__':
    socketio.run(app)
