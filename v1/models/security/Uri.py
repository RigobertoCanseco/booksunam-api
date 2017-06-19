from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load


class Uri(db.Model):
    """
    Data Model: Table 'SEC_URIS'
    """
    __tablename__ = 'SEC_URIS'
    id = db.Column(db.String(32), primary_key=True, autoincrement=True, nullable=False, name="ID")
    uri = db.Column(db.String(255), nullable=False, unique=True, name="URI")

    def __init__(self, uri):
        """
        :param uri: 
        """
        self.id = KeysDB.create_id(uri)
        self.uri = uri

    def __repr__(self):
        return "<Uri id='%s', uri='%s'>" % (self.id, self.uri)


# OBJECT MODEL 'URI'
class UriSchema(Schema):
    id = fields.Str()
    uri = fields.Str()

    @post_load
    def make(self, data):
        return Uri(**data)
