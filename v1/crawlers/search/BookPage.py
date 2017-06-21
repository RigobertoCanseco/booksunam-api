# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from flask import request
from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection
from v1.models.library.Search import ResultSchema, BookSchema


class BookPage(object):
    def __init__(self, session, url, args):
        self.session = session
        self.url = url
        self.args = args

    # SEARCH BASIC
    def search_basic(self):
        # GET PARAMETERS
        url = self.url + self.session + '?' + self.get_args_search_basic()

        # GET REQUEST TO LIBRARY
        result = HttpConnection.get_request(url)

        if result is None:
            return None
        else:
            return self.parse_page(result)

    def get_args_search_basic(self):
        pass

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
            return {"message": "Servicio no disponible", "status": "KO"}

    def get_args_pagination(self):
        pass

    def search_multi_field(self, params):
        pass

    def search_advanced(self, params):
        pass

    # INDEX ALPHABETIC
    def index_by_title(self):
        pass

    def index_by_theme(self):
        pass

    def index_by_editorial(self):
        pass

    def parse_page(self, result):
        soup_result = BeautifulSoup(result, "html.parser", from_encoding = 'utf-8')
        # GET <TITLE>
        title = soup_result.head.title.text

        # WHAT PAGE IS?
        if title == "LIBROS - Registro":
            return self.parse_page_register(soup_result.body)
        elif title == "LIBROS - Resultados":
            return self.parse_page_result(soup_result.body)
        else:
            return None

    # <!-- filename: (login)login-session -->
    # <title>LIBROS - Registro</title>
    def parse_page_register(self, body):
        pass

    # <!-- filename: short-2-head  -->
    # <title>LIBROS - Resultados</title>
    def parse_page_result(self, body):
        book_schema = BookSchema()
        result_schema = ResultSchema()

        soup_result_body = body

        # GET TYPE SORT
        p_sort = soup_result_body.find(id = "ordenamiento").p
        set_number = CleanHTML.get_set_number(p_sort.find_all("a")[0]['href'])

        # NUMBER OF RESULTS
        div_navigation = soup_result_body.find(id = "navRegistros")
        total = div_navigation.find("li", class_ = "txtStrong paddLeft")
        total = CleanHTML.clean_total(total.text)

        # NEXT PAGE
        next_page = div_navigation.find("a", title = "Next")
        prev_page = div_navigation.find("a", title = "Previous")
        link_next = ""
        link_prev = ""
        if next_page is not None:
            jump = CleanHTML.get_jump(next_page['href'])
            link_next = str(request.url_root) + "api/v1" + '/search?' \
                        + 'library=' + self.args["library"] \
                        + '&collection=' + self.args["collection"] \
                        + '&type=' + self.args["type"] \
                        + '&session=' + self.session + '&start=' + jump
        if prev_page is not None:
            jump = CleanHTML.get_jump(prev_page['href'])
            link_prev = str(request.url_root) + "api/v1" + '/search?' \
                        + 'library=' + self.args["library"] \
                        + '&collection=' + self.args["collection"] \
                        + '&type=' + self.args["type"] \
                        + '&session=' + self.session + '&start=' + jump

        # RESULTS
        div = soup_result_body.find(id = "resultSetSearch")
        table = div.table
        table_body_result = table.find_all("tbody")
        books = []
        for t_body in table_body_result:
            # ROWS
            tr = t_body.tr

            # FIELD NUMBER
            id_number = tr.find("td", class_ = "td0").a.text
            item = CleanHTML.get_set_entry(tr.find("td", class_ = "td0").a['href'])

            # FIELD AUTHOR
            author = CleanHTML.clean_blank_space(tr.find("td", class_ = "td1l").text).replace(",autor", "")

            # FIELD TITLE
            title = CleanHTML.clean_blank_space(tr.find("td", class_ = "td2l").text)

            # FIELD CLASSIFICATION
            classification = CleanHTML.clean_blank_space(tr.find("td", class_ = "td4l").text)

            # FIELD COPIES
            copies = tr.find("td", class_ = "td5l").a
            copies_dic = CleanHTML.clean_copies(copies.text)
            link_copies = str(request.url_root) + "api/v1" + '/search?' + 'session=' + self.session \
                          + '&doc_number=' + CleanHTML.get_doc_number(copies['href']) \
                          + '&doc_library=' + CleanHTML.get_doc_library(copies['href']) \
                          + '&sub_library=' + CleanHTML.get_sub_library(copies['href'])

            # LINK ITEM
            link = str(request.url_root) + "api/v1" + '/search?' + 'session=' + self.session + "&set_number=" \
                   + set_number + '&item=' + item

            book, errors = book_schema.load({
                "id": int(id_number),
                "author": author,
                "title": title,
                "classification": classification,
                "link": link,
                "link_copies": link_copies,
                "copies": copies_dic["copies"],
                "on_loan": copies_dic["on_loan"],
            })
            books.append(book)

        result, errors = result_schema.load({
            "session": self.session,
            "set_number": set_number,
            "books": books,
            "total": total,
            "next": link_next,
            "prev": link_prev
        })

        if len(errors) > 0:
            print errors
            return None

        return result

    def detail(self, session, set_number, set_entry):
        self.session = session
        result = HttpConnection.get_request(self.url + '/' + self.session + '?' + 'func=full-set-set&set_number='
                                            + set_number + "&set_entry=" + set_entry + "&format=999")
        if result is not None:
            soup_result = BeautifulSoup(result, from_encoding = 'utf-8')
            soup_result_body = soup_result.body
            div = soup_result_body.find(id = "resultSetSearch")
            table = div.table
            trs = table.find_all("tr")
            info = []

            numero_sistema_th = trs[0].find("th")
            numero_sistema_td = trs[0].find("td")

            clasificacion_th = trs[1].find("th")
            clasificacion_td = trs[1].find("td")

            clasificacion_dewey_th = trs[2].find("th")
            clasificacion_dewey_td = trs[2].find("td")

            ISBN_th = trs[3].find("th")
            ISBN_td = trs[3].find("td")

            autor_th = trs[4].find("th")
            autor_td = trs[4].find("td")

            titulo_th = trs[5].find("th")
            titulo_td = trs[5].find("td")

            datos_de_publicacion_th = trs[6].find("th")
            datos_de_publicacion_td = trs[6].find("td")

            anio_th = trs[7].find("th")
            anio = trs[7].find("td")

            descripcion_fisica_th = trs[8].find("th")
            descripcion_fisica_td = trs[8].find("td")

            return {"message": "Servicio no disponible", "status": "KO"}
        else:
            return {"message": "Servicio no disponible", "status": "KO"}

