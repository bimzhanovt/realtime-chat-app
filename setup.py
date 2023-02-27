from setuptools import setup

setup(
    name='realtime_chat',
    packages=['realtime_chat'],
    include_package_data=True,
    install_requires=[
        'Flask==2.2.3',
        'Flask-SQLAlchemy==3.0.3',
        'Flask-WTF==1.1.1',
        'WTForms==3.0.1',
        'Flask-Login==0.6.2',
    ],
)

from realtime_chat import app
from realtime_chat.models import db

with app.app_context():
    db.drop_all()
    db.create_all()
