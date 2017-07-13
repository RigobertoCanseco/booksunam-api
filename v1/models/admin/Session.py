import datetime
from dateutil.relativedelta import *
from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load
from v1.models.admin.Client import ClientSchema
from v1.models.admin.User import UserSchema


def get_expiration():
    return datetime.datetime.now() + relativedelta(months = +1)


# DATA MODEL 'SESSION'
class Session(db.Model):
    """
    Data Model: Table 'ADM_SESSIONS'
    """
    __tablename__ = 'ADM_SESSIONS'
    user_id = db.Column(db.String(32), db.ForeignKey("ADM_USERS.ID"), primary_key=True, nullable=False, name="USER_ID")
    client_id = db.Column(db.String(32), db.ForeignKey("ADM_CLIENTS.ID"), primary_key=True, nullable=False, unique=True,
                          name="CLIENT_ID")
    token = db.Column(db.String(32), nullable=False, unique=True, name="TOKEN")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    expiration_time = db.Column(db.DateTime, default=get_expiration(), onupdate = get_expiration(), name="EXPIRATION_TIME")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")

    # Relationships
    user = db.relationship("User", backref=db.backref("sessions", lazy="dynamic"))
    client = db.relationship("Client", backref=db.backref("sessions", lazy="dynamic"))

    def __init__(self, user_id, client_id, token=None, active=True, status=0, type=0, expiration_time=None, creation_time=None,
                 update_time=None):
        """
        :param user_id: 
        :param client_id: 
        :param active: 
        :param status: 
        :param type: 
        :param expiration_time: 
        :param creation_time: 
        :param update_time: 
        """
        self.user_id = user_id
        self.client_id = client_id
        if token is None:
            self.token = KeysDB.uuid()
        else:
            self.token = token

        self.active = active
        self.status = status
        self.type = type
        self.expiration_time = expiration_time
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<Session user_id='%s', client_id='%s', token='%s', active='%s', status='%s', type='%s', " \
               "expiration_time='%s', creation_time='%s', update_time='%s'>" \
               % (self.user_id, self.client_id, self.token, self.active, self.status, self.type, self.expiration_time,
                  self.creation_time, self.update_time)


# OBJECT MODEL 'SESSION'
class SessionSchema(Schema):
    user_id = fields.Str()
    client_id = fields.Str()
    token = fields.Str()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    user = fields.Nested(UserSchema)
    client = fields.Nested(ClientSchema)

    @post_load
    def make(self, data):
        return Session(**data)
