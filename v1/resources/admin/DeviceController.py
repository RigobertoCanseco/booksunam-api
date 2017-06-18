# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.admin.Device import DeviceSchema
# DATA MODEL
from v1.models.admin.Device import Device
# EXCEPTIONS
# from api.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from api.common import Status
# AUTHENTICATION
# from api import auth


class DeviceController(Controller):
    def __init__(self):
        super(DeviceController, self).__init__(DeviceSchema, Device)


class DeviceListController(ControllerList):
    def __init__(self):
        super(DeviceListController, self).__init__(DeviceSchema, Device)
