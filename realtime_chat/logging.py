import logging

from realtime_chat import app

logging.basicConfig(
    format=f'%(asctime)s %(levelname)s {app.name}: %(message)s',
    level=logging.INFO
)

LOG_MESSAGES = {
    'user_signup': 'User signed up.',
    'user_unsuccessful_signup': 'Unsuccessful attempt to sign up.',
    'user_login': 'User logged in.',
    'user_unsuccessful_login': 'Unsuccessful attempt to log in.',
    'user_logout': 'User logged out.',
}

def log_user_action(log_message, username):
    """
    Logs a user action with the specified log message and username.

    Parameters:
    log_message (str): The log message to be logged. Use the keys in
                       `LOG_MESSAGES` to ensure consistent log messages.
    username (str): The username associated with the user action.

    Returns:
    None

    Example:
    >>> log_user_action(LOG_MESSAGES['user_signup'], 'John')
    User signed up. {"username": "John"}
    """
    logging.info(log_message + f' {{"username": "{username}"}}')
