from urllib import urlencode

from v1.common.CleanHTML import CleanHTML
from v1.models.library.Search import BookSearchSchema, ResultSearchSchema
from v1.crawlers.library.BookPage import BookPage
from flask import request


class BookItem(BookPage):
    def __init__(self, session, url, args):
        self.key = 'l0801'
        self.args = args
        super(BookItem, self).__init__(session, url, args)

    def get_args_search_basic(self):
        if "from_year" not in self.args:
            self.args["from_year"] = ""

        if "to_year" not in self.args:
            self.args["to_year"] = ""

        p = urlencode({
            "func":"find-b",
            "local_base": self.key,
            "request": self.args["request"],
            "find_code": self.args["field"],
            "adjacent":  self.args["split"],
            "filter_code1": "WLN",
            "filter_request_1": self.args["language"],
            "filter_code_2":  "WYR",
            "filter_request_2":  self.args["from_year"],
            "filter_code_3": "WYR",
            "filter_request_3":  self.args["to_year"]
        }, 'utf-8')
        return p

    def get_args_pagination(self):
        p = urlencode({
            "func": "short-jump",
            "jump": self.args["start"]
        }, 'utf-8')
        return p

        # <!-- filename: short-2-head  -->
        # <title>LIBROS - Resultados</title>

    def parse_page_result(self, body):
        book_schema = BookSearchSchema()
        result_schema = ResultSearchSchema()

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
                        + '&collection=' + self.args["collection"].lower() \
                        + '&type=' + self.args["type"] \
                        + '&session=' + self.session + '&start=' + jump + "&request=" + self.args["request"]
        if prev_page is not None:
            jump = CleanHTML.get_jump(prev_page['href'])
            link_prev = str(request.url_root) + "api/v1" + '/search?' \
                        + 'library=' + self.args["library"] \
                        + '&collection=' + self.args["collection"].lower() \
                        + '&type=' + self.args["type"] \
                        + '&session=' + self.session + '&start=' + jump + "&request=" + self.args["request"]

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

    def parse_page_view_complete(self):
        book_schema = BookSearchSchema()
        result_schema = ResultSearchSchema()

        trs = body.find(id = "resultSetSearch").table.find_all("tr")

        for tr in trs:
            print tr.th.text , ":" , tr.td