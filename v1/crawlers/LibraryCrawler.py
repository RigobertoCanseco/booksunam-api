# -*- coding: utf-8 -*-

# ADDS LIBRARIES CODE HERE
from v1.crawlers.library.aragon.AragonLibrary import AragonLibrary
from v1.crawlers.library.central.CentralLibrary import CentralLibrary


class LibraryCrawler:
    """
    Crawler main
    * search
    * login
    * session user
    """
    def __init__(self, library_name, url, session=None):
        # CREATE DYNAMICALLY LIBRARY
        class_name = globals()[library_name + "Library"]
        self.libraryAbstract = class_name(url, session=session)

    def search(self, args):
        """
        Search collections
        :param args:
        :return:
        """
        return self.libraryAbstract.search(args)

    def pagination(self, args):
        """
        Get next pagination
        :param args:
        :return:
        """
        return self.libraryAbstract.pagination(args)

    def view_detail(self, args):
        """
        Get detail of item
        :param args:
        :return:
        """
        return self.libraryAbstract.view_detail(args)

    def info_borrow(self, args):
        return self.libraryAbstract.info_borrow(args)

    def login(self, args):
        """
        Create login
        :param args:
        :return:
        """
        return self.libraryAbstract.login(args)

    def logout_session(self, args):
        return self.libraryAbstract.logout_session

    def get_session(self):
        """
        Get session of library
        :return:
        """
        return self.libraryAbstract.get_session()

    def get_available(self):
        """
        Get if library is available
        :return:
        """
        return self.libraryAbstract.get_available()

    def index(self):
        pass
