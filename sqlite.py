from realtime_chat import app
from realtime_chat.models import db

with app.app_context():
    db.drop_all()
    db.create_all()
