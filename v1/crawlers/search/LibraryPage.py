# -*- coding: utf-8 -*-
# HTTP REQUEST
# TOOL FOR CRAWLER WEBSITE
from bs4 import BeautifulSoup
# CLEAN AND PARSE HTML
from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection
# IMPLEMENTS
from v1.exceptions import ExceptionMsg
from aragon.BookItem import BookItem


class LibraryPage(object):
    def __init__(self, url, session=None):
        self.url = url
        self.session = session
        self.available = False

        # IS SERVICE_UNAVAILABLE?
        if HttpConnection.get_request(self.url) is not None:
            # SESSION IS NONE?
            if self.session is None:
                # GET SESSION
                self.session = self.get_html_session()
                # SESSION IS OK
                if self.session is not None:
                    self.available = True
            else:
                # VALIDATE IF IS ACTIVE SESSION
                if self.session_is_active():
                    self.available = True
                else:
                    # GET SESSION
                    self.session = self.get_html_session()
                    # SESSION IS OK
                    if self.session is not None:
                        self.available = True

    def get_html_session(self):
        """
        Get session page
        :return: 
        """
        page = HttpConnection.get_request(self.url)
        if page is None:
            return None

        # CRAWLER PAGE START
        soup_page = BeautifulSoup(page, "html.parser", from_encoding='utf-8')
        meta = soup_page.find_all("meta")[3]
        # CLEAN STRING
        return CleanHTML.clean_session(meta['content'])

    def session_is_active(self):
        page = HttpConnection.get_request(self.url + self.session + '?func=find-b')
        if page is None:
            return False
        # CRAWLER PAGE START
        soup_page = BeautifulSoup(page, "html.parser", from_encoding='utf-8')
        title = soup_page.head.title.text
        if title == "LIBROS - Registro":
            return False
        return True

    def search(self, args):
        """
        Search 
        :param args: 
        :return: 
        """
        function_name = "search_" + args["type"]
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

    def pagination(self, args):
        """
        Search 
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

    def index(self, args):
        class_name = globals()[args["collection"] + "Item"]
        item_abstract = class_name(self.session, self.url)

        # NAME FUNCTION
        function_name = "index_by_" + args["type"]
        try:
            func = getattr(item_abstract, function_name)
        except AttributeError:
            print 'function not found "%s" (%s)' % (function_name, args)
        else:
            return func(args)

    def login(self, login_source, library, count, password):
        pass

    def logout(self):
        pass

    def recover_password(self, identification, credential, count, mail):
        pass

    def get_collection(self):
        soup_page = BeautifulSoup(HttpConnection.get_request(self.url))
        soup_body = soup_page.body
        div = soup_body.find(id="catalogos")
        lis = div.find_all("li")
        links = []
        i = 0
        for li in lis:
            a = li.a
            links.append({
                "text": a.text,
                "link": a['href']
            })
            i += 1
        return links

    def get_session(self):
        return self.session

    def get_available(self):
        return self.available
