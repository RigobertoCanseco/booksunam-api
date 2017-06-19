from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load


class Role(db.Model):
    """
    Data Model: Table 'SEC_ROLES'
    """
    __tablename__ = 'SEC_ROLES'
    id = db.Column(db.String(32), primary_key=True, nullable=False, name="ID")
    role = db.Column(db.String(32), nullable=False, unique=True, name="ROLE")

    def __init__(self, role):
        """
        :param role: 
        """
        self.id = KeysDB.create_id(role)
        self.role = role

    def __repr__(self):
        return "<Role id='%s', role='%s'>" % (self.id, self.role)


# OBJECT MODEL 'ROLE'
class RoleSchema(Schema):
    id = fields.Str()
    role = fields.Str()

    @post_load
    def make(self, data):
        return Role(**data)
