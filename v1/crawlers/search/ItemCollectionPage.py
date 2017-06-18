# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from flask import request

from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection


class ItemCollectionPage(object):

    def __init__(self, session, url):
        self.session = session
        self.url = url

    # SEARCH
    def search_basic(self):
        # GET PARAMETERS
        parameters = self.get_parameters_basic()
        url = self.url + self.session + '?' + parameters

        # GET REQUEST TO LIBRARY
        result = HttpConnection.get_request(url)

        if result is None:
            return None
        else:
            return self.parse_page(result)

    def get_parameters_basic(self):
        pass

    def search_multi_field(self, params):
        pass

    def get_parameters_multi_field(self):
        pass

    def search_advanced(self, params):
        pass

    def get_parameters_advanced(self):
        pass

    # INDEX ALPHABETIC
    def index_by_title(self):
        pass

    def index_by_theme(self):
        pass

    def index_by_editorial(self):
        pass

    def parse_page(self, result):
        soup_result = BeautifulSoup(result, "html.parser", from_encoding='utf-8')
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
        soup_result_body = body

        div_ordenamiento = soup_result_body.find(id="ordenamiento")
        p_ordenamiento = div_ordenamiento.p
        links_ordenamiento = p_ordenamiento.find_all("a")
        ordenamiento = []
        for link in links_ordenamiento:
            ordenamiento.append({'type': link.text, 'link': link['href']})

        divNavigation = soup_result_body.find(id="navRegistros")
        total = divNavigation.find("li", class_="txtStrong paddLeft")
        total = CleanHTML.clean_total(total.text)

        nextNavigation = divNavigation.find("a", title="Next")
        previousNavigation = divNavigation.find("a", title="Previous")

        div = soup_result_body.find(id="resultSetSearch")
        table = div.table
        tbodys = table.find_all("tbody")
        books = []
        for tbody in tbodys:
            tr = tbody.tr
            link = tr.find("td", class_="td0")
            a = link.a
            num = a.text

            autor = tr.find("td", class_="td1l")
            autor = CleanHTML.clean_blank_space(autor.text)
            autor = autor.replace(",autor", "")

            titulo = tr.find("td", class_="td2l")

            titulo = CleanHTML.clean_blank_space(titulo.text)

            clasificacion = tr.find("td", class_="td4l")
            clasificacion = CleanHTML.clean_blank_space(clasificacion.text)
            ejemplares = tr.find("td", class_="td5l")
            a3 = ejemplares.a

            # autor_unicode = unidecode(autor.text)
            # titulo_unicode = unidecode(titulo.text)
            # clasificacion_unicode = unidecode(clasificacion.text)
            # ejemplares_unicode = unidecode(a3.text)

            number = CleanHTML.clean_number(a['href'])
            entry = CleanHTML.clean_entry(a['href'])
            link = str(request.url_root) + 'todo/api/v1.0/book/session/' + self.session + "/number/" + number \
                   + '/entry/' + entry
            books.append({
                "_id": int(num),
                #  "link": link,
                "author": autor,
                "title": titulo,
                "classification": clasificacion,
                "copies": CleanHTML.clean_copies(a3.text),
                #  "link_copies": a3['href']
            })

        dic = {
            "session": self.session,
            "sort": ordenamiento,
            "books": books,
            "total": int(total)
        }

        # if nextNavigation is not None:
        #     # dic['next'] = nextNavigation['href']
        #     block = self.block(nextNavigation['href'])
        #     dic['next'] = str(request.url_root) + 'todo/api/v1.0/book/session/' + self.session + "/block/" + block
        #
        # if previousNavigation is not None:
        #     # dic['previous'] = previousNavigation['href']
        #     block = self.block(previousNavigation['href'])
        #     dic['previous'] = str(request.url_root) + 'todo/api/v1.0/book/session/' + self.session + "/block/" + block

        return dic

    def detail(self, session, set_number, set_entry):
        self.session = session
        result = HttpConnection.get_request(self.url + '/' + self.session + '?' + 'func=full-set-set&set_number='
                                            + set_number + "&set_entry=" + set_entry + "&format=999")
        if result is not None:
            soup_result = BeautifulSoup(result, from_encoding='utf-8')
            soup_result_body = soup_result.body
            div = soup_result_body.find(id="resultSetSearch")
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

    # http://biblioteca-fes.aragon.unam.mx:8991/F/KDI2PDGKFEJQT5CGQN5U2316HNJJG6R6JRMQE8HFHJG9DCYKV9-06200
    # ?func=full-set-set&set_number=000089&set_entry=000001&format=999
    def block(self, block):
        # http://biblioteca-fes.aragon.unam.mx:8991/F/DCG4KLUGTU92SRS8HLY2LD2M9V8TPRELXXH2LQAMR6Y1MF7SYD-16392?func
        # =short-jump&jump=000001
        result = HttpConnection.get_request(self.url + '/' + self.session + '?' + 'func=short-jump&jump=' + block)
        if result is not None:
            return self.parse_page(result)
        else:
            return {"message": "Servicio no disponible", "status": "KO"}
