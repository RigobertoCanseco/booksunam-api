from v1.flaskapp import db


class Permission(db.Model):
    """
    Data Model: Table 'ADM_PERMISSIONS'
    """
    __tablename__ = 'ADM_PERMISSIONS'
    role_id = db.Column(db.Integer, db.ForeignKey('ADM_ROLES.ID'), primary_key=True, nullable=False, name="ROLE_ID")
    uri_id = db.Column(db.Integer, db.ForeignKey('ADM_URIS.ID'), primary_key=True, nullable=False, name="URI_ID")
    verb_id = db.Column(db.Integer, db.ForeignKey('ADM_VERBS.ID'), primary_key=True,nullable=False, name="VERB_ID")

    def __init__(self, role_id=int, uri_id=int, verb_id=int):
        """
        :param role_id: 
        :param uri_id: 
        :param verb_id: 
        """
        self.role_id = role_id
        self.uri_id = uri_id
        self.verb_id = verb_id

