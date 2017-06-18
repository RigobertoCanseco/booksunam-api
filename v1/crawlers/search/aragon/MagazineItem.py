from v1.crawlers.search.ItemCollectionPage import ItemCollectionPage


class MagazineItem(ItemCollectionPage):
    @staticmethod
    def __new__(cls, *more):
        return super(MagazineItem, cls).__new__(cls, *more)

    def __init__(self, session, url):
        super(MagazineItem, self).__init__(session, url)
