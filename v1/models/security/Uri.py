from v1.flaskapp import db


class Uri(db.Model):
    """
    Data Model: Table 'ADM_URIS'
    """
    __tablename__ = 'ADM_URIS'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, name="ID")
    uri = db.Column(db.String(255), nullable=False, unique=True, name="URI")

    def __init__(self, id=int, uri=str):
        """
        :param id: 
        :param uri: 
        """
        self.id = id
        self.uri = uri

    def __repr__(self):
        return '<Uri %r>' % (self.uri)