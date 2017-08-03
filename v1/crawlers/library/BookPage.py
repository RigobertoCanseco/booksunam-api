# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection


class BookPage(object):
    def __init__(self, session, url, args):
        self.session = session
        self.url = url
        self.args = args
        self.type = 1

    """
    PARSE PAGES
    """
    def parse_page(self, result):
        """
        PARSE PAGES
        :param result:
        :return:
        """
        soup_result = BeautifulSoup(result, "html.parser", from_encoding = 'utf-8')
        # GET <TITLE>
        title = soup_result.head.title.text

        # WHAT PAGE IS?
        if title == "LIBROS - Resultados":
            return self.parse_page_result(soup_result.body)
        elif title == "LIBROS - Vista completa del registro ":
            # GET VIEW OF ELEMENT IN FORMAT SET/VALUE
            if "entry" not in self.args or self.args["entry"] is None or "set_number" not in self.args or self.args["set_number"] is None:
                self.args["set_number"] = CleanHTML.get_set_number(soup_result.body.find_all("ul")[3].li.a['href'])
                self.args["entry"] = "000001"
                book = self.detail()
                return book

            else:
                result = result.replace("<th", "<td")
                soup_result = BeautifulSoup(result, "html.parser", from_encoding = 'utf-8')
                book = self.parse_page_view_complete(soup_result.body)
                return book
                # self.args["number_system"] = book["number_system"]
                # # GET INFO BORROW BOOK
                # book["borrow_detail"] = self.info_borrow_book()
                # book["id"] = int(self.args["entry"])
                # book["entry"] = '{:06}'.format(int(self.args["entry"]))
                #
                # result, errors = result_schema.load({
                #     "session": self.session,
                #     "set_number": self.args["set_number"],
                #     "books": book,
                #     "total": 1
                # })
                # if len(errors) > 0:
                #     print errors
                #     return None
                #
                # return result

        elif title == "LIBROS - Acervo":
            soup_result = BeautifulSoup(re.sub(r'<table class="filtro">(.|\n)*?<\/table>', "", result),
                                        "html.parser", from_encoding = 'utf-8')
            return self.parse_page_info_borrow_book(soup_result)
        else:
            return None

    """
    SEARCH TYPES
    """
    def search_basic(self):
        """
        Search basic option
        :return:
        """
        # GET PARAMETERS
        url = self.url + self.session + '?' + self.get_args_search_basic()

        # GET REQUEST TO LIBRARY
        result = HttpConnection.get_request(url)

        if result is None:
            return None
        else:
            return self.parse_page(result)

    def search_multi_field(self, params):
        pass

    def search_advanced(self, params):
        pass

    """
    PAGINATION
    """
    def pagination(self):
        """
        Pagination
        :return:
        """
        url = self.url + self.session + '?' + self.get_args_pagination()
        result = HttpConnection.get_request(url)
        if result is not None:
            return self.parse_page(result)
        else:
            return None

    """
    VIEW DETAIL ITEM    
    """
    def detail(self):
        url = self.url + self.session + '?' + self.get_args_detail()
        result = HttpConnection.get_request(url)
        if result is not None:
            return self.parse_page(result)
        else:
            return None

    """
    GET INFO BORROW BOOK   
    """
    def info_borrow(self):
        url = self.url + self.session + '?' + self.get_args_info_borrow_book()
        result = HttpConnection.get_request(url)
        if result is not None:
            return self.parse_page(result)
        else:
            return None

    """
    IMPLEMENT
    """
    def get_args_search_basic(self):
        pass

    def get_args_pagination(self):
        pass

    def get_args_detail(self):
        pass

    def get_args_info_borrow_book(self):
        pass

    def parse_page_result(self, body):
        pass

    def parse_page_view_complete(self, body):
        pass

    def parse_page_info_borrow_book(self, body):
        pass

    # INDEX ALPHABETIC
    def index_by_title(self):
        pass

    def index_by_theme(self):
        pass

    def index_by_editorial(self):
        pass