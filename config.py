import os

from dotenv import load_dotenv

load_dotenv()

USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
SERVER=os.getenv('SERVER')
DB=os.getenv('DB')

DEBUG = True

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.getenv('FLASK_SECRET')
BABEL_DEFAULT_LOCALE = 'pt'
