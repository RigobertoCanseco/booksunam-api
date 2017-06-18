# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.library.Library import LibrarySchema
# DATA MODEL
from v1.models.library.Library import Library
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from v1.common import Status
# AUTHENTICATION
# from api import auth

"""
http://oreon.dgbiblio.unam.mx/F/
"""


class LibraryController(Controller):
    def __init__(self):
        super(LibraryController, self).__init__(LibrarySchema, Library)


class LibraryListController(ControllerList):
    def __init__(self):
        super(LibraryListController, self).__init__(LibrarySchema, Library)