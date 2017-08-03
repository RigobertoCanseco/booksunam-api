# coding=utf-8
from urllib import urlencode
from v1.crawlers.library.BookPage import BookPage
from v1.common.CleanHTML import CleanHTML
from v1.models.library.Search import BookSearchSchema, ResultSearchSchema
from flask import request


class BookItem(BookPage):
    def __init__(self, session, url, args):
        self.key = 'l1001'
        super(BookItem, self).__init__(session, url, args)

    def get_args_search_basic(self):
        if "from_year" not in self.args:
            self.args["from_year"] = ""

        if "to_year" not in self.args:
            self.args["to_year"] = ""

        p = urlencode({
            "func": "find-b",
            "local_base": self.key,
            "request": self.args["request"],
            "find_code": self.args["field"],
            "adjacent": self.args["split"],
            "filter_code1": "WLN",
            "filter_request_1": self.args["language"],
            "filter_code_2": "WYR",
            "filter_request_2": self.args["from_year"],
            "filter_code_3": "WYR",
            "filter_request_3": self.args["to_year"]
        }, 'utf-8')
        return p

    def get_args_pagination(self):
        return urlencode({
            "func": "short-jump",
            "jump": self.args["start"]
        }, 'utf-8')

    def get_args_detail(self):
        return urlencode({
            "func": "full-set-set",
            "set_number": self.args["set_number"],
            "set_entry": self.args["entry"],
            "format": "002"
        }, 'utf-8')

    def get_args_info_borrow_book(self):
        return urlencode({
            "func": "item-global",
            "doc_library": str(self.key).upper(),
            "doc_number": self.args["number_system"],
            "year": "",
            "volume": "",
            "sub_library": ""
        }, 'utf-8')

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
            entry = '{:06}'.format(int(id_number))
            item = CleanHTML.get_set_entry(tr.find("td", class_ = "td0").a['href'])

            # FIELD AUTHOR
            author = CleanHTML.clean_blank_space(tr.find("td", class_ = "td1l").text).replace(",autor", "")

            # FIELD TITLE
            title = CleanHTML.clean_blank_space(CleanHTML.get_title(tr.find("td", class_ = "td2l").text))

            # FIELD CLASSIFICATION
            classification = CleanHTML.clean_blank_space(tr.find("td", class_ = "td4l").text)

            # FIELD COPIES
            copies = tr.find("td", class_ = "tdJoker").a

            # NUMBER SYSTEM
            number_system = CleanHTML.get_doc_number(copies['href'])
            copies_dic = CleanHTML.clean_copies(copies.text)

            link_detail = str(request.url_root) + "api/v1" + '/search?' \
                          + 'session=' + self.session \
                          + '&library=' + self.args["library"] \
                          + '&collection=' + self.args["collection"].lower() \
                          + '&set_number=' + set_number \
                          + '&entry=' + entry \
                          + '&type=' + self.args["type"] \
                          + "&request=" + self.args["request"]

            link_borrow = str(request.url_root) + "api/v1" + '/search?' \
                          + 'session=' + self.session \
                          + '&library=' + self.args["library"] \
                          + '&collection=' + self.args["collection"].lower() \
                          + '&number_system=' + number_system \
                          + '&type=' + self.args["type"] \
                          + "&request=" + self.args["request"]

            book, errors = book_schema.load({
                "id": int(id_number),
                "library_id": self.args["library"],
                "entry": entry,
                "author": author,
                "title": title,
                "number_system": number_system,
                "classification": classification,
                "copies": copies_dic["copies"],
                "on_loan": copies_dic["on_loan"],
                "link_detail": link_detail,
                "link_borrow_info": link_borrow
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

    def parse_page_view_complete(self, body):
        book_schema = BookSearchSchema()
        result_schema = ResultSearchSchema()

        trs = body.find(id = "resultSetSearch").table.find_all("tr")
        data = dict()
        for tr in trs:
            tds = tr.find_all("td")
            if tds[0].text.encode('utf-8') in data:
                if type(data[tds[0].text.encode('utf-8')]) is not list:
                    tmp = data[tds[0].text.encode('utf-8')]
                    data[tds[0].text.encode('utf-8')] = [tmp]
                data[tds[0].text.encode('utf-8')].append(tds[1].text)
            else:
                data[tds[0].text.encode('utf-8')] = tds[1].text
        t = u'Título'
        c = u'Clasificación'
        b = {
            "id": int(self.args["entry"]),
            "entry": '{:06}'.format(int(self.args["entry"])),
            "library_id": self.args["library"],
            "author": data["Autor"].replace("autor.", "")[2:],
            "title": data[t.encode('utf-8')][2:],
            "classification": data[c.encode('utf-8')][2:],
            "number_system": data["No. de sistema"][1][1:],
            "type": self.type
        }

        # DELETE DATA RIPET
        del data["Autor"], data[t.encode('utf-8')], data[c.encode('utf-8')], data["No. de sistema"]
        b["detail"] = data

        book, errors = book_schema.load(b)
        if len(errors) > 0:
            print errors
            return None

        result, errors = result_schema.load({
            "session": self.session,
            "set_number": self.args["set_number"],
            "books": [book],
            "total": 1
        })
        if len(errors) > 0:
            print errors
            return None

        return result

    def parse_page_info_borrow_book(self, body):
        book_schema = BookSearchSchema()
        result_schema = ResultSearchSchema()
        trs = body.find(id = "resultSetSearch").find_all("table")[2].find_all("tr")
        h = []
        for th in trs[0].find_all("th"):
            h.append(th.text)
        l = []
        for i in range(1, len(trs)):
            o = {}
            tds = trs[i].find_all("td")
            for j in range(len(tds)):
                o[h[j]] = tds[j].text
            l.append(o)

        b = {
            "library_id": self.args["library"],
            "number_system": self.args["number_system"],
            "type": self.type,
            "borrow_detail": l
        }

        book, errors = book_schema.load(b)
        if len(errors) > 0:
            print errors
            return None

        result, errors = result_schema.load({
            "session": self.session,
            "books": [book],
            "total": 1
        })
        if len(errors) > 0:
            print errors
            return None

        return result
