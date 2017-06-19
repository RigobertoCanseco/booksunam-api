from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load


class Verb(db.Model):
    """
    Data Model: Table 'SEC_VERBS'
    """
    __tablename__ = 'SEC_VERBS'
    id = db.Column(db.String(32), primary_key=True, nullable=False, name="ID")
    verb = db.Column(db.String(32), nullable=False, unique=True, name="VERB")

    def __init__(self, verb):
        """
        :param verb: 
        """
        self.id = KeysDB.create_id(verb)
        self.verb = verb

    def __repr__(self):
        return "<Verb id='%s', verb='%s'>" % (self.id, self.verb)


# OBJECT MODEL 'VERB'
class VerbSchema(Schema):
    id = fields.Str()
    verb = fields.Str()

    @post_load
    def make(self, data):
        return Verb(**data)
