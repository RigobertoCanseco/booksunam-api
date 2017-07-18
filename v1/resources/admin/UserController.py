# -*- coding: utf-8 -*-
# CONTROLLER
import datetime

from v1.resources.Controller import Controller, ControllerList, IntegrityError, OperationalError, SQLAlchemyError
# OBJECT MODEL
from v1.models.admin.User import UserSchema
# DATA MODEL
from v1.models.admin.User import User
from v1.models.security.Role import RoleSchema, Role
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
from v1.common import Status
# AUTHENTICATION
from v1 import db


class UserController(Controller):
    def __init__(self):
        super(UserController, self).__init__(UserSchema, User, ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])


class UserListController(ControllerList):
    def __init__(self):
        super(UserListController, self).__init__(UserSchema, User, ['GET'])

    def post(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # VALIDATE JSON DATA
        if not self.json_data:
            return ExceptionMsg.message_to_json_invalid(), Status.HTTP.BAD_REQUEST

        try:

            user, errors = self.schema.load(self.json_data)

            # # SERIALIZER JSON TO LIBRARY MODEL
            # if self.client.id == '33ca8c20fc3207a5e31f85b11ffdd886':
            #     role_schema = RoleSchema()
            #     role, errors = role_schema.load(dict(id='2e40ad879e955201df4dedbf8d479a12', role='USER'))
            #     #self.json_data['roles'] = [dict(id='2e40ad879e955201df4dedbf8d479a12', role='USER')]
            #     user.roles.append(role)

            if len(errors) > 0:
                return ExceptionMsg.message_to_bad_request(errors), Status.HTTP.BAD_REQUEST
        except Exception as e:
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR

        # INSERT TO DATA BASE
        try:
            db.session.add(user)
            db.session.commit()
            result = self.schema.dump(user)
            # SEND MAIL

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
