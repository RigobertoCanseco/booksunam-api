# -*- coding: utf-8 -*-
# RESTFUL
from flask import jsonify, render_template, send_from_directory
from flask_restful import reqparse, Resource
from sqlalchemy.exc import *
# APP, DATABASE, AUTHENTICATION
from v1 import app, db, auth
# EXCEPTIONS
from v1.common import Status
from v1.exceptions.ExceptionMsg import ExceptionMsg


# HANDLERS
# NOT_FOUND
@app.errorhandler(404)
def page_not_found(a):
    return jsonify(ExceptionMsg.set_message_error(100000, "Elemento no encontrado", {})), Status.HTTP.NOT_FOUND


# METHOD_NOT_ALLOWED
@app.errorhandler(405)
def method_not_allowed(a):
    return jsonify(ExceptionMsg.set_message_error(100000, "Método no permitido", {})), Status.HTTP.METHOD_NOT_ALLOWED


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

    def __init__(self, Schema, Model):
        self.errors = None
        self.model = Model
        request = reqparse.request
        if request.method == 'GET':
            self.schema = Schema()

        elif request.method == 'PUT':
            self.schema = Schema()

        elif request.method == 'PATCH':
            self.schema = Schema()

        elif request.method == 'DELETE':
            self.schema = Schema()

        elif request.method == 'POST':
            if request.data == "" or request.content_length == 0:
                self.errors = ("bad_request", Status.HTTP.BAD_REQUEST)
            elif request.mimetype != 'application/json':
                self.errors = ("not_json", Status.HTTP.BAD_REQUEST)
            else:
                self.json_data = request.json
            self.schema = Schema()

        super(Controller, self).__init__()

    def get(self, id):
        # SELECT IN  DATA BASE
        try:
            library = self.model.query.get(id)
            result = self.schema.dump(library)
            return result.data, Status.HTTP.OK
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR

    def put(self, id):
        # SELECT IN  DATA BASE
        try:
            library = self.model.query.get(id)
            result = self.schema.dump(library)
            return result.data, Status.HTTP.OK
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR

    def patch(self, id):
        # SELECT IN  DATA BASE
        try:
            library = self.model.query.get(id)
            result = self.schema.dump(library)
            return result.data, Status.HTTP.OK
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR

    def delete(self, id):
        # SELECT IN  DATA BASE
        try:
            library = self.model.query.get(id)
            result = self.schema.dump(library)
            return result.data, Status.HTTP.OK
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR


class ControllerList(Resource):
    """

    """
    decorators = [auth.login_required]

    def __init__(self, Schema, Model):
        self.errors = None
        self.model = Model
        request = reqparse.request
        if request.method == 'POST':
            if request.data == "" or request.content_length == 0 or type(request.data) is str:
                self.errors = ("bad_request", Status.HTTP.NO_CONTENT)
            elif request.mimetype != 'application/json':
                self.errors = ("not_json", Status.HTTP.UNPROCESSABLE_ENTITY)
            elif type(request.json) is str:
                self.errors = ("bad_request", Status.HTTP.NO_CONTENT)
            else:
                self.json_data = request.json
            self.schema = Schema()
        elif request.method == 'GET':
            self.schema = Schema(many=True)

        super(ControllerList, self).__init__()

    def post(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return ExceptionMsg.get_message_error(self.errors[0]), self.errors[1]

        # VALIDATE JSON DATA
        if not self.json_data:
            return ExceptionMsg.set_message_error(100001, "Se espera un json", {}), Status.HTTP.NOT_FOUND

        # SERIALIZER JSON TO LIBRARY MODEL
        library, errors = self.schema.load(self.json_data)

        # INSERT TO DATA BASE
        try:
            db.session.add(library)
            db.session.commit()
            result = self.schema.dump(library)
            return result.data, Status.HTTP.CREATED
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.set_message_error(100001, e.message, {}), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.set_message_error(100002, e.message, {}), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            return ExceptionMsg.set_message_error(100003, e.message, {}), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR

    def get(self):
        # SELECT IN  DATA BASE
        try:
            library = self.model.query.all()
            result = self.schema.dump(library)
            return result.data, Status.HTTP.OK
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR
