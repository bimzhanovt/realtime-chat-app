from flask_login import LoginManager

from realtime_chat import app
from realtime_chat.models import User

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
