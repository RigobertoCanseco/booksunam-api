# -*- coding: utf-8 -*-
# CONTROLLER
from v1.resources.Controller import Controller, ControllerList
# OBJECT MODEL
from v1.models.library.Book import BookSchema
# DATA MODEL
from v1.models.library.Book import Book
# EXCEPTIONS
# from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
# from v1.common import Status
# AUTHENTICATION
# from api import auth


class BookController(Controller):
    def __init__(self):
        super(BookController, self).__init__(BookSchema, Book)


class BookListController(ControllerList):
    def __init__(self):
        super(BookListController, self).__init__(BookSchema, Book)
