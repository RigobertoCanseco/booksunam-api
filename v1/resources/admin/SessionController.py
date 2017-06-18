# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.admin.Session import SessionSchema
# DATA MODEL
from v1.models.admin.Session import Session
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from v1.common import Status


class SessionController(Controller):
    def __init__(self):
        super(SessionController, self).__init__(SessionSchema, Session)


class SessionListController(ControllerList):
    def __init__(self):
        super(SessionListController, self).__init__(SessionSchema, Session)
