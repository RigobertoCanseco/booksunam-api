# -*- coding: utf-8 -*-
# RESTFUL
import datetime
from flask import jsonify, render_template, send_from_directory
from flask_restful import reqparse, Resource
from sqlalchemy.exc import *
# APP, DATABASE, AUTHENTICATION
from v1.models.admin.Session import Session, SessionSchema
from v1.models.admin.Client import Client
from v1 import app, db, auth
# EXCEPTIONS
from v1.common import Status
from v1.exceptions.ExceptionMsg import ExceptionMsg


# HANDLERS
# NOT_FOUND
@app.errorhandler(404)
def page_not_found(a):
    return jsonify(ExceptionMsg.message_to_page_not_found()), Status.HTTP.NOT_FOUND


@app.errorhandler(500)
def server_error(a):
    return jsonify(ExceptionMsg.message_to_server_error("unknown, :) ....")), Status.HTTP.INTERNAL_SERVER_ERROR


# METHOD_NOT_ALLOWED
@app.errorhandler(405)
def method_not_allowed(a):
    return jsonify(ExceptionMsg.message_to_method_not_allowed()), Status.HTTP.METHOD_NOT_ALLOWED


users = {
    "admin": "S3cr3T"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/secret-page')
@auth.login_required
def other():
    return "Hello, %s!" % auth.username()


@app.route('/<path:resource>')
def serve_static_resource(resource):
    return send_from_directory('static/', resource)


class Controller(Resource):
    decorators = [auth.login_required]

    def __init__(self, Schema, Model, token_required):
        self.errors = None
        self.model = Model
        self.token_required = token_required
        request = reqparse.request

        # GET CLIENT
        self.client = Client.query.filter_by(token = request.headers.get("Client-Token")).first()
        if self.client is None or self.client.active is False:
            self.errors = (ExceptionMsg.message_to_bad_token_client(), Status.HTTP.UNAUTHORIZED)
        else:
            # GET SESSION
            self.user_token = request.headers.get("User-Token")
            if request.method == 'GET':
                self.schema = Schema()

            elif request.method == 'PUT':
                self.schema = Schema()

            elif request.method == 'PATCH':
                self.schema = Schema()

            elif request.method == 'DELETE':
                self.schema = Schema()

            elif request.method == 'POST':
                self.errors = (ExceptionMsg.message_to_method_not_allowed(), Status.HTTP.METHOD_NOT_ALLOWED)

                # if request.data == "" or request.content_length == 0:
                #     self.errors = (ExceptionMsg.message_to_not_content(), Status.HTTP.BAD_REQUEST)
                # elif request.mimetype != 'application/json':
                #     self.errors = (ExceptionMsg.message_to_not_json(), Status.HTTP.BAD_REQUEST)
                # else:
                #     self.json_data = request.json
                # self.schema = Schema()

        super(Controller, self).__init__()

    def get(self, id):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'GET' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        # SESSION DUMP
        # session_schema = SessionSchema()
        # session = session_schema.dump(session)

        # VALIDATE TOKEN SESSION WITH  USER ID
        # if not id == session.data['user']['id']:
        #   return ExceptionMsg.set_message_error(101001, "Token is invalid", {}), Status.HTTP.METHOD_NOT_ALLOWED

        # SELECT IN  DATA BASE
        try:
            data = self.model.query.get(id)
            if data is None:
                return ExceptionMsg.message_to_object_not_found(), Status.HTTP.NOT_FOUND
            result = self.schema.dump(data)
            return result.data, Status.HTTP.OK
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR

    def put(self, id):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'PUT' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        # SESSION DUMP
        # session_schema = SessionSchema()
        # session = session_schema.dump(session)

        # SELECT IN DATA BASE
        try:
            data = self.model.query.get(id)
            if data is None:
                return ExceptionMsg.message_to_object_not_found(), Status.HTTP.NOT_FOUND
            result = self.schema.dump(data)
            return result.data, Status.HTTP.OK
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR

    def patch(self, id):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'PATCH' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        # SESSION DUMP
        # session_schema = SessionSchema()
        # result = session_schema.dump(session)

        # SELECT IN DATA BASE
        try:
            data = self.model.query.get(id)
            if data is None:
                return ExceptionMsg.message_to_object_not_found(), Status.HTTP.NOT_FOUND
            result = self.schema.dump(data)
            return result.data, Status.HTTP.OK
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR

    def delete(self, id):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'DELETE' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        # SESSION DUMP
        # session_schema = SessionSchema()
        # result = session_schema.dump(session)

        # SELECT IN  DATA BASE
        try:
            data = self.model.query.get(id)
            if data is None:
                return ExceptionMsg.message_to_object_not_found(), Status.HTTP.NOT_FOUND
            result = self.schema.dump(data)
            return result.data, Status.HTTP.OK
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR


class ControllerList(Resource):
    """

    """
    decorators = [auth.login_required]

    def __init__(self, Schema, Model, token_required):
        self.errors = None
        self.model = Model
        self.token_required = token_required
        request = reqparse.request

        # GET CLIENT
        self.client = Client.query.filter_by(token = request.headers.get("Client-Token")).first()

        if self.client is None or self.client.active is False:
            self.errors = (ExceptionMsg.message_to_bad_token_client(), Status.HTTP.UNAUTHORIZED)
        else:
            # GET SESSION
            self.user_token = request.headers.get("User-Token")
            if request.method == 'POST':
                if request.data == "" or request.content_length == 0 or type(request.data) is not str:
                    self.errors = (ExceptionMsg.message_to_not_json(), Status.HTTP.BAD_REQUEST)
                elif request.mimetype != 'application/json':
                    self.errors = (ExceptionMsg.message_to_not_json(), Status.HTTP.BAD_REQUEST)
                elif type(request.json) is str:
                    self.errors = (ExceptionMsg.message_to_not_content(), Status.HTTP.NO_CONTENT)
                else:
                    self.json_data = request.json
                self.schema = Schema()
            elif request.method == 'GET':
                self.schema = Schema(many=True)

        super(ControllerList, self).__init__()

    def post(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'POST' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        # SESSION DUMP
        # session_schema = SessionSchema()
        # session = session_schema.dump(session)

        try:
            # VALIDATE JSON DATA
            if not self.json_data:
                return ExceptionMsg.message_to_json_invalid(), Status.HTTP.BAD_REQUEST
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR

        # SERIALIZER JSON TO OBJECT MODEL
        try:
            schema, errors = self.schema.load(self.json_data)
            if len(errors) > 0:
                return ExceptionMsg.message_to_bad_request(errors), Status.HTTP.BAD_REQUEST
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR
        # VALIDATE TOKEN SESSION WITH  USER ID
        # if 'user_id' in self.json_data:
        #    if not schema.user_id == session.data['user']['id']:
        #        return ExceptionMsg.set_message_error(101001, "Token is invalid", {}), Status.HTTP.METHOD_NOT_ALLOWED

        # INSERT TO DATA BASE
        try:
            db.session.add(schema)
            db.session.commit()
            result = self.schema.dump(schema)
            return result.data, Status.HTTP.CREATED
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR

    def get(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'GET' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        # SESSION DUMP
        # session_schema = SessionSchema()
        # result = session_schema.dump(session)

        # SELECT IN  DATA BASE
        try:
            data = self.model.query.all()
            if data is None:
                return ExceptionMsg.message_to_object_not_found(), Status.HTTP.NOT_FOUND
            result = self.schema.dump(data)
            return result.data, Status.HTTP.OK
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR
