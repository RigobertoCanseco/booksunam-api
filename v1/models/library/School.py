from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load


# DATA MODEL 'SCHOOL'
class School(db.Model):
    """
    Data Model: Table 'LIB_SCHOOLS'
    """
    __tablename__ = 'LIB_SCHOOLS'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    name = db.Column(db.String(64), nullable=False, name="NAME")
    address = db.Column(db.String(128), nullable=False, name="ADDRESS")
    website = db.Column(db.String(128), nullable=True, name="WEBSITE")
    mail = db.Column(db.String(128), nullable=True, name="MAIL")
    telephone = db.Column(db.String(16), nullable=True, name="TELEPHONE")
    latitude = db.Column(db.DECIMAL, nullable=True, name="LATITUDE")
    longitude = db.Column(db.DECIMAL, nullable=True, name="LONGITUDE")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")

    def __init__(self, name, address=None, website=None, mail=None, telephone=None, latitude=None, longitude=None,
                 active=True, status=0, type=0, creation_time=None, update_time=None):
        """        
        :param name: 
        :param address: 
        :param website: 
        :param mail: 
        :param telephone: 
        :param latitude: 
        :param longitude: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        self.id = KeysDB.create_id(name.encode("utf-8"))
        self.name = name
        self.address = address
        self.website = website
        self.mail = mail
        self.telephone = telephone
        self.latitude = latitude
        self.longitude = longitude
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<Schools id='%s', name='%s', address='%s', website='%s', mail='%s', telephone='%s', latitude='%s', " \
               "longitude='%s', active='%s', status='%s',  type='%s', creation_time'%s', update_time='%s'>" \
               % (self.id, self.name, self.address, self.website, self.mail, self.telephone, self.latitude,
                  self.longitude, self.active, self.status, self.type, self.creation_time, self.update_time)


# OBJECT MODEL 'SCHOOL'
class SchoolSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    address = fields.Str()
    website = fields.Str()
    mail = fields.Str()
    telephone = fields.Str()
    latitude = fields.Decimal()
    longitude = fields.Decimal()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()

    @post_load
    def make_user(self, data):
        return School(**data)
