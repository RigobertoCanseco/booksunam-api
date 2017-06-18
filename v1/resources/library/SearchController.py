# -*- coding: utf-8 -*-
from flask_restful import reqparse
# CONTROLLER
from v1.resources.Controller import ControllerList
# OBJECT MODEL
from v1.models.library.Search import SearchSchema
from v1.models.library.Library import LibrarySchema
# DATA MODEL
from v1.models.library.Library import Library
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
# STATUS CODES
from v1.common import Status
# CRAWLER
from v1.crawlers.search.SearchCrawler import SearchCrawler

# from pprint import pprint
# import sys, urllib2
# reload(sys)
# sys.setdefaultencoding("latin-1")


class SearchListController(ControllerList):
    def __init__(self):
        request = reqparse.request
        if request.method == 'GET':
            # GET ARGUMENTS
            super(SearchListController, self).__init__(SearchSchema, Library)
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
        search_schema = SearchSchema()
        self.args, errors = search_schema.load(args)
        if len(errors) > 0:
            return ExceptionMsg.set_message_error(101001, errors, {}), Status.HTTP.BAD_REQUEST

        # REPLACE VALUES
        search_schema.replace_values(self.args)

        try:
            # SELECT IN DATA BASE
            libraryOM = library_schema.dump(self.model.query.get(self.args['library']))
            if len(libraryOM.data) == 0:
                return ExceptionMsg.set_message_error(101001, "Biblioteca no encontrada", {}), Status.HTTP.BAD_REQUEST
            session = "RK7DB519X9JRH79RPYATX2EL1PMC6CSFJMAHMIIFI5TDJ4CTAM-01873"
            # CREATE NEW SEARCH CRAWLER
            search_crawler = SearchCrawler(libraryOM.data["class_name"], libraryOM.data["website"], session=session)

            # GET PAGE
            if not search_crawler.get_available():
                return ExceptionMsg.set_message_error(101001, "Servicio no disponible", {}),\
                       Status.HTTP.SERVICE_UNAVAILABLE

            # GET SESSION DATA
            session = search_crawler.get_session()
            print session

            result = search_crawler.search(self.args)

            return result, Status.HTTP.OK
        except Exception as e:
            print e
            return ExceptionMsg.set_message_error(101001, e.message, {}), Status.HTTP.INTERNAL_SERVER_ERROR
