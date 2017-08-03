# -*- coding: utf-8 -*-
import datetime

from flask_restful import reqparse

# CRAWLER
from crawlers.LibraryCrawler import LibraryCrawler
# STATUS CODES
from v1.common import Status
# EXCEPTIONS
from v1.exceptions.ExceptionMsg import ExceptionMsg
from v1.models.admin.Session import Session
# DATA MODEL
from v1.models.library.Library import Library
from v1.models.library.Library import LibrarySchema
# OBJECT MODEL
from v1.models.library.SessionLIbrary import SessionLibrarySchema
# CONTROLLER
from v1.resources.Controller import ControllerList


# from pprint import pprint
# import sys, urllib2
# reload(sys)
# sys.setdefaultencoding("latin-1")


class SessionLibraryController(ControllerList):
    def __init__(self):
        super(SessionLibraryController, self).__init__(SessionLibrarySchema, Library, ['POST'])

    def post(self):
        # VALIDATE ERRORS
        if self.errors is not None:
            return self.errors[0], self.errors[1]

        # CHECK SESSION
        # session = None
        if 'POST' in self.token_required:
            session = Session.query.filter_by(token = self.user_token).first()
            if session is None or not session.active or session.expiration_time < datetime.datetime.now():
                return ExceptionMsg.message_to_session_invalid(), Status.HTTP.UNAUTHORIZED

        args = reqparse.request.args
        if args is None:
            return ExceptionMsg.message_to_bad_request("Not found arguments"), Status.HTTP.BAD_REQUEST
        if len(args) is 0:
            return ExceptionMsg.message_to_bad_request("Not found arguments"), Status.HTTP.BAD_REQUEST

        # SERIALIZER
        library_schema = LibrarySchema()
        search_schema = SessionLibrarySchema()
        self.args, errors = search_schema.load(args.to_dict())
        if len(errors) > 0:
            return ExceptionMsg.message_to_bad_request(errors), Status.HTTP.BAD_REQUEST

        try:
            # SELECT IN DATA BASE
            library_om = library_schema.dump(self.model.query.get(self.args['library']))
            if len(library_om.data) == 0:
                return ExceptionMsg.message_to_bad_request("Library not found"), Status.HTTP.BAD_REQUEST

            # GET SESSION
            if "session" in self.args:
                session = self.args["session"]
            else:
                session = None
            # CREATE NEW SEARCH CRAWLER
            search_crawler = LibraryCrawler(library_om.data["class_name"], library_om.data["website"], session=session)

            # PAGE IS UNAVAILABLE
            if not search_crawler.get_available():
                return ExceptionMsg.message_to_server_error("Service not unavailable"), Status.HTTP.SERVICE_UNAVAILABLE

            # GET SESSION DATA
            session = search_crawler.get_session()

            result = search_crawler.login(self.args)

            return result, Status.HTTP.OK
        except Exception as e:
            print e
            return ExceptionMsg.message_to_server_error(e.message), Status.HTTP.INTERNAL_SERVER_ERROR
