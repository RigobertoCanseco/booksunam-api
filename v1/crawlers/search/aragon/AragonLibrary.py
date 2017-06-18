# -*- coding: utf-8 -*-
from v1.crawlers.search.LibraryPage import LibraryPage


# CRAWLER FOR 'ARAGON WEBSITE'
class AragonLibrary(LibraryPage):
    def __init__(self, url, session):
        super(AragonLibrary, self).__init__(url=url, session=session)

