from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load


# DATA MODEL 'CLIENT'
class Client(db.Model):
    """
    Data Model: Table 'ADM_CLIENTS'
    """
    __tablename__ = 'ADM_CLIENTS'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    name = db.Column(db.String(128), nullable=False, name="NAME")
    token = db.Column(db.String(256), nullable=False, name="TOKEN")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")

    def __init__(self, name, active=True, status=0, type=0, creation_time=None, update_time=None):
        """
        :param name:
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """

        self.id = KeysDB.create_id(name.encode("utf-8"))
        self.token = KeysDB.uuid()
        self.name = name
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<Client id='%s', name='%s', token='%s', active='%s', status='%s', type='%s', creation_time='%s'," \
               " update_time='%s'>" \
               % (self.id, self.name, self.token, self.active, self.status, self.type, self.creation_time,
                  self.update_time)


# OBJECT MODEL 'CLIENT'
class ClientSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    token = fields.Str()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()

    @post_load
    def make_user(self, data):
        return Client(**data)
