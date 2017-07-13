# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.admin.User import UserSchema
# DATA MODEL
from v1.models.admin.Session import Session
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from api.common import Status
# AUTHENTICATION
# from api import auth


class LogoutController(Controller):
    def __init__(self):
        super(LogoutController, self).__init__(UserSchema, Session)

    def post(self):
        pass
