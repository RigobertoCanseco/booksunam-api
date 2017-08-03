# -*- coding: utf-8 -*-
from v1.crawlers.library.LibraryPage import LibraryPage
from v1.crawlers.library.aragon.BookItem import BookItem
from v1.crawlers.library.aragon.Session import Session


class AragonLibrary(LibraryPage):
    def __init__(self, url, session):
        super(AragonLibrary, self).__init__(url=url, session=session)

    def search(self, args):
        """
        Search collection
        :param args:
        :return: Object to result
        """
        # NAME OF FUNCTION
        function_name = "search_" + args["type"]
        # CREATE INSTANCE DYNAMICALLY
        try:
            #
            class_name = globals()[args["collection"] + "Item"]
            item_abstract = class_name(self.session, self.url, args)
            # NAME FUNCTION
            func = getattr(item_abstract, function_name)
        except AttributeError:
            print 'function not found %s' % function_name
        else:
            return func()

    def view_detail(self, args):
        """
        View detail of item
        :param args:
        :return: Object to result
        """
        # NAME OF FUNCTION
        function_name = "detail_" + args["type"]
        # CREATE INSTANCE DYNAMICALLY
        try:
            #
            class_name = globals()[args["collection"] + "Item"]
            item_abstract = class_name(self.session, self.url, args)
            # NAME FUNCTION
            func = getattr(item_abstract, function_name)
        except AttributeError:
            print 'function not found %s' % function_name
        else:
            return func()

    def pagination(self, args):
        """
        Search pagination
        :param args:
        :return:
        """
        function_name = "pagination"
        # CREATE INSTANCE DYNAMICALLY
        try:
            class_name = globals()[args["collection"] + "Item"]
            item_abstract = class_name(self.session, self.url, args)
            # NAME FUNCTION
            func = getattr(item_abstract, function_name)
        except AttributeError:
            print 'function not found %s' % function_name
        else:
            return func()

    def login(self, args):
        # NAME OF FUNCTION
        function_name = "login"
        # CREATE INSTANCE DYNAMICALLY
        try:
            #
            class_name = globals()["Session"]
            item_abstract = class_name(self.session, self.url, args)
            # NAME FUNCTION
            func = getattr(item_abstract, function_name)
        except AttributeError:
            print 'function not found %s' % function_name
        else:
            return func()

    def logout(self):
        pass