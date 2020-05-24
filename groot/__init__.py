from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from groot.config import * 

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)