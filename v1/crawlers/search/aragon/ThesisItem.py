from v1.crawlers.search.ItemCollectionPage import ItemCollectionPage


class ThesisItem(ItemCollectionPage):
    @staticmethod
    def __new__(cls, *more):
        return super(ThesisItem, cls).__new__(cls, *more)

    def __init__(self, session, url):
        super(ThesisItem, self).__init__(session, url)
