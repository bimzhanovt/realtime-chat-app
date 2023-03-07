from flask_login import current_user
from flask_socketio import join_room, emit

from realtime_chat import socketio
from realtime_chat.chat_validators import *
from realtime_chat.models import *

@socketio.on('join')
def on_join(room):
    if not current_user.is_authenticated:
        return False

    if not validate_room(room):
        emit('error', INVALID_DATA_MESSAGE)
        return

    if not Chat.query.get(room):
        emit('error', CHAT_NOT_FOUND_MESSAGE)
        return

    join_room(room)

@socketio.on('message')
def on_message(message):
    if not current_user.is_authenticated:
        return False

    if not validate_message(message):
        emit('error', INVALID_DATA_MESSAGE)
        return

    if not Chat.query.get(message['room']):
        emit('error', CHAT_NOT_FOUND_MESSAGE)
        return

    chat_message = ChatMessage(chat_id=message['room'],
        user_id=current_user.id, text=message['text'])

    emit('message',
        {
            'username': current_user.username,
            'text': message['text'],
            'time': chat_message.time.strftime('%H:%M'),
        },
        to=message['room'],
    )
