# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.admin.User import UserSchema
# DATA MODEL
from v1.models.admin.User import User
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from api.common import Status
# AUTHENTICATION
# from api import auth


class UserController(Controller):
    def __init__(self):
        super(UserController, self).__init__(UserSchema, User)


class UserListController(ControllerList):
    def __init__(self):
        super(UserListController, self).__init__(UserSchema, User)
