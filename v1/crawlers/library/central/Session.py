from v1.crawlers.library.SessionPage import SessionPage


class Session(SessionPage):
    def __init__(self, session, url, args):
        self.key = 'l0801'
        self.args = args
        super(Session, self).__init__(session, url, args)