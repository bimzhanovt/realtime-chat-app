from wtforms.validators import Length, Regexp

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 25

USERNAME_REGEXP = r'^[a-z_][a-z0-9_]*$'
USERNAME_REGEXP_MESSAGE = 'Username must start with a letter or underscore and contain only letters, numbers, or underscores'

USERNAME_VALIDATORS = [
    Length(min=MIN_USERNAME_LENGTH, max=MAX_USERNAME_LENGTH),
    Regexp(USERNAME_REGEXP, message=USERNAME_REGEXP_MESSAGE),
]

PASSWORD_HASH_LENGTH = 128
