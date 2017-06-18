from urllib import urlencode

from v1.crawlers.search.ItemCollectionPage import ItemCollectionPage


class BookItem(ItemCollectionPage):
    def __init__(self, session, url, args):
        self.key = 'l0801'
        self.args = args

        super(BookItem, self).__init__(session, url)

    def get_parameters_basic(self):

        if "from_year" not in self.args:
            self.args["from_year"] = ""

        if "to_year" not in self.args:
            self.args["to_year"] = ""

        param = "func=" + "find-b" +\
                "&local_base=" + self.key +\
                "&request=" + self.args["request"] +\
                "&find_code=" + self.args["field"] +\
                "&adjacent=" + self.args["split"] +\
                "&filter_code1=" + "WLN" +\
                "&filter_request_1=" + self.args["language"] +\
                "&filter_code_2=" + "WYR" +\
                "&filter_request_2=" + self.args["from_year"] +\
                "&filter_code_3=" + "WYR" +\
                "&filter_request_3=" + self.args["to_year"]

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
        print p
        return p

    def get_parameters_multi_field(self):
        s = ""
        return s

    def get_parameters_advanced(self):
        s = ""
        return s
