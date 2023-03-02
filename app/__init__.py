from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

from .views import backup_view
from .views import frequency_view
from .views import relatory_view
