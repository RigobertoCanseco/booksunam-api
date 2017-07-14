# -*- coding: utf-8 -*-
from flask_restful import reqparse
# CONTROLLER
from v1.resources.Controller import ControllerList
# OBJECT MODEL
from v1.models.library.Library import LibrarySchema, Library
from v1.models.library.NewBook import QueryNewBooksSchema
# DATA MODEL
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
from v1.common import Status
# CRAWLER
from v1.crawlers.news.NewsBooksCrawler import NewsBooksCrawler

# from pprint import pprint
# import sys, urllib2
# reload(sys)
# sys.setdefaultencoding("latin-1")


class NewBookListController(ControllerList):
    def __init__(self):
        request = reqparse.request
        if request.method == 'GET':
            # GET ARGUMENTS
            super(NewBookListController, self).__init__(QueryNewBooksSchema, Library, [])
        else:
            self.args = None
            self.errors = ("method_invalid", Status.HTTP.METHOD_NOT_ALLOWED)

    def get(self):
        # str_request = urllib2.quote(str_request.encode('utf-8'))
        # str_type_search = request.form['type_search']
        args = reqparse.request.args
        if args is None:
            return ExceptionMsg.set_message_error(101001, "Parametros faltantes", {}), Status.HTTP.BAD_REQUEST
        if len(args) is 0:
            return ExceptionMsg.set_message_error(101001, "Parametros faltantes", {}), Status.HTTP.BAD_REQUEST

        # SERIALIZER
        library_schema = LibrarySchema()
        query_news_books = QueryNewBooksSchema()
        self.args, errors = query_news_books.load(args)
        if len(errors) > 0:
            return ExceptionMsg.set_message_error(101001, errors, {}), Status.HTTP.BAD_REQUEST

        # REPLACE VALUES
        query_news_books.replace_values(self.args)

        try:
            # SELECT IN DATA BASE
            library_om = library_schema.dump(self.model.query.get(self.args['library']))
            if len(library_om.data) == 0:
                return ExceptionMsg.set_message_error(101001, "Biblioteca no encontrada", {}), Status.HTTP.BAD_REQUEST

            # CREATE  NEW BOOKS CRAWLER
            crawler = NewsBooksCrawler()

            # GET BOOKS
            result = crawler.search(library_om.data["key"], self.args["date_from"], self.args["date_to"],
                                    self.args["base"], self.args["order"], self.args["term"], self.args["index"],
                                    self.args["init"], self.args["total"])

            return result, Status.HTTP.OK
        except Exception as e:
            print e
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR