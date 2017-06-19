# -*- coding: utf-8 -*-
from aragon import AragonLibrary


class SearchCrawler:
    def __init__(self, library_name, url, session=None):
        self.library_name = library_name
        self.url = url
        self.result = None

        # CREATE DYNAMICALLY LIBRARY
        class_name = globals()[self.library_name + "Library"]
        self.libraryAbstract = class_name(url, session=session)

    def search(self, args):
        return self.libraryAbstract.search(args)

    def pagination(self, args):
        return self.libraryAbstract.pagination(args)

    def index(self):
        pass

    def get_session(self):
        return self.libraryAbstract.get_session()

    def get_available(self):
        return self.libraryAbstract.get_available()


