# coding=utf-8
import datetime
from bs4 import BeautifulSoup
from urllib import urlencode
from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection
from v1.models.library.NewBook import ResultSearchSchema, NewBookItemSchema


class NewsBooksCrawler:
    def __init__(self):
        self.url = "http://132.248.9.32/alerta/alerta.php"
        self.consult = "http://132.248.9.32/alerta/consulta.php"

    def get_args_search(self, library, date_from, date_to, base, order=None, term=None, index=None, init=None,
                        total=None):
        if term is None:
            term = ""
        if index is None:
            index = "title"
        if order is None:
            order = "title"

        # year_limit = '{:02d}'.format(date_to.year - date_from.year)
        # month_limit = '{:02d}'.format(date_to.month - date_from.month)
        a = {
            "base": base,
            "year1": str(date_from.year),
            "year2": str(date_to.year),
            "mesini": '{:02d}'.format(date_from.month),
            "mesfin": '{:02d}'.format(date_to.month),
            "termino": term,
            "indice": index,
            "orden": order,
            "clavebib": library,
        }
        if total is not None:
            a["total"] = total
        if init is not None:
            a["init"] = init
        p = urlencode(a, 'utf-8')
        return p

    def search(self, library, date_from, date_to, base, order=None, term=None, index=None, init=None, total=None):
        """
        :param library: 
        :param date_from: 
        :param date_to: 
        :param base: 
        :param order: 
        :param term: 
        :param index: 
        :param init: 
        :param total: 
        :return: 
        """
        params = self.get_args_search(library, date_from, date_to, base, order, term, index, init, total)
        # GET REQUEST
        result = HttpConnection.get_request(self.consult + '?' + params)
        if result is None:
            return None

        result_schema = ResultSearchSchema()
        book_schema = NewBookItemSchema()

        soup_result = BeautifulSoup(result, "html.parser", from_encoding = 'utf-8')
        total = CleanHTML.clean_total_registros(soup_result.find_all("tr")[1].td.text)
        books = []
        tr_list = soup_result.find_all("tr")
        for tr in tr_list:
            td = tr.find("td", class_= "texto")
            if td is not None:
                # \|.*?.[ ]{2}
                link = None
                file = None
                try:
                    file = HttpConnection.get_request(tr.contents[2].contents[0].contents[5]["src"])
                    link = CleanHTML.get_link_img_google(file)
                except Exception as e:
                    pass
                # print tr.contents[0].text, "|", tr.contents[1].text, "|", tr.contents[2].contents[0].a["href"], "|",link
                book, errors = book_schema.load({
                    "id": tr.contents[0].text,
                    "classification": tr.contents[1].contents[0],
                    "link_google_books": tr.contents[2].contents[0].a["href"],
                    "info_google": file,
                    "image": link
                })
                books.append(book)

        result, errors = result_schema.load({
            "total": total,
            "books": books,
            "next": "",
            "prev": ""
        })

        if len(errors) > 0:
            print errors
            return None

        return result
