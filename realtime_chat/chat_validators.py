from realtime_chat.constants import *

def validate_room(room):
    return isinstance(room, int)

def validate_message_text(text):
    return isinstance(text, str) and \
        MIN_MESSAGE_TEXT_LENGTH <= len(text) <= MAX_MESSAGE_TEXT_LENGTH

def validate_message(message):
    return isinstance(message, dict) and \
        all(key in message for key in ['room', 'text']) and \
        validate_room(message['room']) and \
        validate_message_text(message['text'])
