# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.library.School import SchoolSchema
# DATA MODEL
from v1.models.library.School import School
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from v1.common import Status
# AUTHENTICATION
# from api import auth


class SchoolController(Controller):
    def __init__(self):
        super(SchoolController, self).__init__(SchoolSchema, School)


class SchoolListController(ControllerList):
    def __init__(self):
        super(SchoolListController, self).__init__(SchoolSchema, School)