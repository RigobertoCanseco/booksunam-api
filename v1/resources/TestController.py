# -*- coding: utf-8 -*-
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.library.Library import LibrarySchema
# DATA MODEL
from v1.models.library.Library import Library
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
from v1.common import Status


class TestController(Controller):
    def __init__(self):
        super(TestController, self).__init__(LibrarySchema, Library)

    def get(self, id):
        # SELECT IN  DATA BASE
        try:
            library = Library.query.get(id)
            result = self.schema.dump(library)
            return {"test":"OK"}, Status.HTTP.OK
        except Exception as e:
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR


class TestListController(ControllerList):
    def __init__(self):
        super(TestListController, self).__init__(LibrarySchema, Library)