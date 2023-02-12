import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Setup
app.secret_key = "ujit1"
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database', 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
api = Api(app)
db = SQLAlchemy(app)
