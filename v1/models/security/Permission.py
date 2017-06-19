from v1 import db
from marshmallow import Schema, fields, post_load
from models.security.Role import RoleSchema
from models.security.Uri import UriSchema
from models.security.Verb import VerbSchema


class Permission(db.Model):
    """
    Data Model: Table 'SEC_PERMISSIONS'
    """
    __tablename__ = 'SEC_PERMISSIONS'
    role_id = db.Column(db.String(32), db.ForeignKey('ADM_ROLES.ID'), primary_key=True, nullable=False, name="ROLE_ID")
    uri_id = db.Column(db.String(32), db.ForeignKey('ADM_URIS.ID'), primary_key=True, nullable=False, name="URI_ID")
    verb_id = db.Column(db.String(32), db.ForeignKey('ADM_VERBS.ID'), primary_key=True, nullable=False, name="VERB_ID")

    # Relationships
    role = db.relationship("Role", backref = db.backref("permission", lazy = "dynamic"))
    uri = db.relationship("Uri", backref = db.backref("permission", lazy = "dynamic"))
    verb = db.relationship("Verb", backref = db.backref("permission", lazy = "dynamic"))

    def __init__(self, role_id, uri_id, verb_id):
        """
        :param role_id: 
        :param uri_id: 
        :param verb_id: 
        """
        self.role_id = role_id
        self.uri_id = uri_id
        self.verb_id = verb_id


# OBJECT MODEL 'PERMISSION'
class PermissionSchema(Schema):
    role_id = fields.Str()
    uri_id = fields.Str()
    verb_id = fields.Str()
    role = fields.Nested(RoleSchema)
    uri = fields.Nested(UriSchema)
    verb = fields.Nested(VerbSchema)

    @post_load
    def make_permission(self, data):
        return Permission(**data)
