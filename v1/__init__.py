from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api


# APP = FLASK APPLICATION
app = Flask(__name__)
# PRODUCTION
app.config.from_pyfile("config/openshift.cfg")
# DEVELOP
#app.config.from_pyfile("config/localhost.cfg")

# DB = DATABASE SQL-ALCHEMY
db = SQLAlchemy()
db.init_app(app)

# AUTH = AUTHENTICATION
auth = HTTPBasicAuth()

# API = FLASK RESTFUL
api = Api(app)
api_version = "/api/v1"



