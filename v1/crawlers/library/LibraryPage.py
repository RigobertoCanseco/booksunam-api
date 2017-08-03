# -*- coding: utf-8 -*-
# HTTP REQUEST
# TOOL FOR CRAWLER WEBSITE
from bs4 import BeautifulSoup
import hashlib
# CLEAN AND PARSE HTML
from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection
# IMPLEMENTS


class LibraryPage(object):
    """
        Class abstract
    """

    def __init__(self, url, session=None):
        """
        Construct
        :param url: URL of library
        :param session: Session of library
        """
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
        Get session page, create new session id
        :return: session
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
        """
        Check if session is active
        :return: Boolean
        """
        page = HttpConnection.get_request(self.url + self.session + '?func=find-b')
        if page is None:
            return False
        # CRAWLER PAGE START
        soup_page = BeautifulSoup(page, "html.parser", from_encoding='utf-8')
        title = soup_page.head.title.text
        # t = u'LIBROS - Búsqueda básica'
        # hast c4908930539677c8dff04d5f1d02ffbc to t
        t = "c4908930539677c8dff04d5f1d02ffbc"
        if hashlib.md5(title.encode('utf-8')).hexdigest() == t:
            return True
        return False

    def logout_session(self):
        page = HttpConnection.get_request(self.url + self.session + '?func=logout')
        if page is None:
            return False
        else:
            return True

    def get_session(self):
        """
        Get session of library
        :return:
        """
        return self.session

    def get_available(self):
        """
        Return if is available library
        :return:
        """
        return self.available

    """
    IMPLEMENTAR
    """
    def search(self, args):
        """
        Search a collection object for example a Book, Thesis or Magazine
        :param args:
        :return:
        """
        pass

    def view_detail(self, args):
        """
        View detail a collection item
        :param args:
        :return:
        """
        pass

    def info_borrow(self, args):
        """
        Return info of borrow book
        :param args:
        :return:
        """
        pass

    def pagination(self, args):
        """
        Get data of pagination with use of link valid
        :param args:
        :return:
        """
        pass

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

    def login(self, args):
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

