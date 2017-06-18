# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.admin.Client import ClientSchema
# DATA MODEL
from v1.models.admin.Client import Client
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from v1.common import Status
# AUTHENTICATION
# from api import auth


class ClientController(Controller):
    def __init__(self):
        super(ClientController, self).__init__(ClientSchema, Client)


class ClientListController(ControllerList):
    def __init__(self):
        super(ClientListController, self).__init__(ClientSchema, Client)
