# -*- coding: utf-8 -*-
# CONTROLLER

from v1.resources.Controller import ControllerList, IntegrityError, OperationalError, SQLAlchemyError
# OBJECT MODEL
from v1.models.admin.User import LoginSchema, User
# DATA MODEL
from v1.models.admin.Session import Session, SessionSchema
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
from v1.common import Status
from v1.common.KeysDB import KeysDB
# AUTHENTICATION
from v1 import db


class LoginController(ControllerList):
    def __init__(self):
        super(LoginController, self).__init__(LoginSchema, Session)

    def post(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return ExceptionMsg.get_message_error(self.errors[0]), self.errors[1]

        # VALIDATE JSON DATA
        if not self.json_data:
            return ExceptionMsg.set_message_error(100001, "Body type not is json", {}), Status.HTTP.NOT_FOUND

        # SERIALIZER JSON TO USER MODEL
        user_model, errors = self.schema.load(self.json_data)
        if len(errors) > 0:
            return ExceptionMsg.set_message_error(101001, errors, {}), Status.HTTP.BAD_REQUEST

        # INSERT TO DATA BASE
        try:
            user = User.query.filter_by(mail =user_model['mail']).first()
            if user is None:
                return ExceptionMsg.set_message_error(100001, "Failed login", {}), Status.HTTP.UNAUTHORIZED
            # COMPARE PASSWORD
            if user.password != KeysDB.password(user_model['password']):
                return ExceptionMsg.set_message_error(100001, "Failed login", {}), Status.HTTP.UNAUTHORIZED

            # FIND SESSION
            session = Session.query.filter_by(user_id = user.id, client_id = self.client.id).first()
            if session is None:
                # CREATE SESSION
                session = Session(user.id, self.client.id)
                db.session.add(session)
                db.session.commit()

            else:
                # UPDATE SESSION
                session.token = KeysDB.uuid()
                db.session.commit()

            # RETURN NEW SESSION
            self.schema = SessionSchema()
            result = self.schema.dump(session)
            return result.data, Status.HTTP.OK
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
