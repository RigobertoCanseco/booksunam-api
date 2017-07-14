# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.admin.Account import AccountSchema
# DATA MODEL
from v1.models.admin.Account import Account
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from v1.common import Status
# AUTHENTICATION
# from api import auth


class AccountController(Controller):
    def __init__(self):
        super(AccountController, self).__init__(AccountSchema, Account, ["GET", "POST", "PUT", "DELETE"])


class AccountListController(ControllerList):
    def __init__(self):
        super(AccountListController, self).__init__(AccountSchema, Account, ["GET", "POST", "PUT", "DELETE"])
