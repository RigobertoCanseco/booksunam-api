# coding=utf-8
import re

from bs4 import BeautifulSoup
from urllib import urlencode

from flask import request

from v1.common.CleanHTML import CleanHTML
from v1.common.HttpConnection import HttpConnection
from v1.models.library.NewBook import ResultSearchSchema, NewBookItemSchema


class NewsBooksCrawler:
    def __init__(self):
        self.url = "http://132.248.9.32/alerta/alerta.php"
        self.consult = "http://132.248.9.32/alerta/consulta.php"

    def get_args_search(self, args):

        term = ""
        index = "titulo"
        order = "titulo"
        if "term" in args and args["term"] is not None:
            term = args["term"]
        if "index" in args and args["index"] is not None:
            index = args["index"]
        if "order" in args and args["order"] is not None:
            index = args["order"]

        a = {
            "base": args["base"],
            "year1": str(args["date_from"].year),
            "year2": str(args["date_to"].year),
            "mesini": "{:02d}".format(args["date_from"].month),
            "mesfin": "{:02d}".format(args["date_to"].month),
            "termino": term,
            "indice": index,
            "orden": order,
            "clavebib": args["library_key"],
            "yearlimite": "",
            "meslimite": "01"
        }
        if "total" in args and args["total"] is not None:
            a["numreg1"] = args["total"]
        a["inicio"] = 0
        if "init" in args and args["init"] is not None:
            a["inicio"] = args["init"]


        p = urlencode(a, "utf-8")
        return p

    def search(self, args):
        """
        :param args
        :return: 
        """
        params = self.get_args_search(args)
        # GET REQUEST
        result = HttpConnection.get_request(self.consult + "?" + params)
        if result is None:
            return None

        result_schema = ResultSearchSchema()
        book_schema = NewBookItemSchema()

        soup_result = BeautifulSoup(result, "html.parser", from_encoding = "utf-8")
        total = int(CleanHTML.clean_total_registros(soup_result.find_all("tr")[1].td.text))
        books = []
        tr_list = soup_result.find_all("tr")
        for tr in tr_list:
            td = tr.find("td", class_= "texto")
            if td is not None:
                # GET INFO TO GOOGLE BOOKS
                link = None
                file = None
                link_google = None
                try:
                    file = HttpConnection.get_request(tr.contents[2].contents[0].contents[5]["src"])
                    link = CleanHTML.get_link_img_google(file)
                    link_google = "https://books.google.com.mx/books?id=" + CleanHTML.get_google_book_id(file) + "&printsec=frontcover"
                except Exception as e:
                    pass

                # PARSE DETAIL
                detail = []
                data = tr.contents[1].contents
                for c in data:
                    try:
                        if c.text != '':
                            detail.append(c.text[:-1])
                    except Exception as e:
                        text = re.sub(r'^\ *', "", c[:-1])
                        if text != '':
                            detail.append(text)


                book, errors = book_schema.load({
                    "id": tr.contents[0].text,
                    "classification": tr.contents[1].contents[0][:-1],
                    # "link_google_books": tr.contents[2].contents[0].a["href"],
                    "link_google_books": link_google,
                    "info_google": file,
                    "image": link,
                    "detail": detail
                })
                books.append(book)

        link_next = None
        link_prev = None

        init = 0
        if "init" in args and args["init"] is not None:
            init = args["init"]

        if args["base"] == "LIBIMP":
            base = "impress"
        else:
            base = "ebook"

        if (int(init) + 20) <= total:
            link_next = str(request.url_root) + "api/v1" + "/news?" \
                        + "library=" + args["library"] \
                        + "&date_from=" + args["date_from"].strftime("%d/%m/%Y") \
                        + "&date_to=" + args["date_to"].strftime("%d/%m/%Y") \
                        + "&base=" + str(base) \
                        + "&total=" + str(total) \
                        + "&init=" + str(int(init) + 20)
        if int(init) != 0:
            link_prev = str(request.url_root) + "api/v1" + "/news?" \
                        + "library=" + args["library"] \
                        + "&date_from=" + args["date_from"].strftime("%d/%m/%Y") \
                        + "&date_to=" + args["date_to"].strftime("%d/%m/%Y") \
                        + "&base=" + base \
                        + "&total=" + str(total) \
                        + "&init=" + str(int(init) - 20)

        result, errors = result_schema.load({
            "total": total,
            "books": books,
            "next": link_next,
            "prev": link_prev
        })

        if len(errors) > 0:
            print errors
            return None

        return result
