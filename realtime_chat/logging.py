from realtime_chat import app

import logging

logging.basicConfig(
    format=f'%(asctime)s %(levelname)s {app.name}: %(message)s',
    level=logging.INFO
)

def log_info(func):
    def wrapper(*args, **kwargs):
        message = func(*args, **kwargs)
        logging.info(message)
    return wrapper

@log_info
def log_user_signup(username):
    return f'User signed up. {{"username": "{username}"}}'

@log_info
def log_user_unsuccessful_sign_up(username):
    return f'Unsuccessful attempt to sign up. {{"username": "{username}"}}'

@log_info
def log_user_login(username):
    return f'User logged in. {{"username": "{username}"}}'

@log_info
def log_user_unsuccessful_log_in(username):
    return f'Unsuccessful attempt to log in. {{"username": "{username}"}}'

@log_info
def log_user_logout(username):
    return f'User logged out. {{"username": "{username}"}}'
