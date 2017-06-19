from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load
from v1.models.admin.User import UserSchema


# DATA MODEL 'DEVICE'
class Device(db.Model):
    """
    Data Model: Table 'ADM_DEVICES'
    """
    __tablename__ = 'ADM_DEVICES'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    name = db.Column(db.String(32), nullable=False, name="NAME")
    user_id = db.Column(db.String(32), db.ForeignKey("ADM_USERS.ID"), nullable=False, name="USER_ID")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")

    # Relationships
    user = db.relationship("User", backref=db.backref("devices", lazy="dynamic"))

    def __init__(self, user_id, name,  active=True, status=0, type=0, creation_time=None, update_time=None):
        """
        :param name: 
        :param user_id: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        self.id = KeysDB.create_id(user_id + name)
        self.name = name
        self.user_id = user_id
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<Device id='%s', user_id='%s', name='%s', active='%s', status='%s', type='%s', creation_time='%s', " \
               "update_time='%s'>" % \
               (self.id, self.user_id, self.name, self.active, self.status, self.type, self.creation_time,
                self.update_time)


# OBJECT MODEL 'DEVICE'
class DeviceSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    user_id = fields.Str()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    user = fields.Nested(UserSchema)

    @post_load
    def make(self, data):
        return Device(**data)
