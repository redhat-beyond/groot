from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from groot.config import *
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
