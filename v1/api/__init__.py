from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
db = SQLAlchemy()
# auth = HTTPBasicAuth()
