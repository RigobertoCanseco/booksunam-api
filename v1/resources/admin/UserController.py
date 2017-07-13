# -*- coding: utf-8 -*-
# CONTROLLER
import datetime

from v1.resources.Controller import Controller, ControllerList, IntegrityError, OperationalError, SQLAlchemyError
# OBJECT MODEL
from v1.models.admin.User import UserSchema
# DATA MODEL
from v1.models.admin.User import User
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
from v1.common import Status
# AUTHENTICATION
from v1 import db


class UserController(Controller):
    def __init__(self):
        super(UserController, self).__init__(UserSchema, User)


class UserListController(ControllerList):
    def __init__(self):
        super(UserListController, self).__init__(UserSchema, User, ['POST'])

    def post(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return ExceptionMsg.get_message_error(self.errors[0]), self.errors[1]

        # CHECK SESSION
        if 'POST' in self.token_required:
            if self.session is None or not self.session.active or self.session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.set_message_error(100001, "Session is invalid", {}), Status.HTTP.UNAUTHORIZED

        # VALIDATE JSON DATA
        if not self.json_data:
            return ExceptionMsg.set_message_error(100001, "Se espera un json", {}), Status.HTTP.NOT_FOUND

        # SERIALIZER JSON TO LIBRARY MODEL
        library, errors = self.schema.load(self.json_data)
        if len(errors) > 0:
            return ExceptionMsg.set_message_error(101001, errors, {}), Status.HTTP.BAD_REQUEST

        # INSERT TO DATA BASE
        try:
            db.session.add(library)
            db.session.commit()
            result = self.schema.dump(library)
            # SEND MAIL

            return result.data, Status.HTTP.CREATED
        except IntegrityError as e:
            print "IntegrityError"
            return ExceptionMsg.set_message_error(100001, e.message, {}), Status.HTTP.CONFLICT
        except OperationalError as e:
            print "OperationalError:"
            return ExceptionMsg.set_message_error(100002, e.message, {}), Status.HTTP.CONFLICT
        except SQLAlchemyError as e:
            print "SQLAlchemyError:"
            print e.message
            return ExceptionMsg.set_message_error(100003, e.message, {}), Status.HTTP.CONFLICT
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR