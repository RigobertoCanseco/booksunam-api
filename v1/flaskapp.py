# coding=utf-8
from flask import render_template, send_from_directory
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources import TestController

#######################################################################################################################
# APP = FLASK APPLICATION
app = Flask(__name__)
app.config.from_pyfile("config/flaskapp.cfg")
########################################################################################################################
# DB = DATABASE SQL-ALCHEMY
db = SQLAlchemy()
db.init_app(app)
########################################################################################################################
# API = FLASK RESTFUL
api = Api(app)
api_version = "/api/v1"
########################################################################################################################


api.add_resource(TestController, '/')


# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/<path:resource>')
# def serve_static_resource(resource):
#     return send_from_directory('static/', resource)


if __name__ == '__main__':
    app.run(app.config['IP'], app.config['PORT'])
