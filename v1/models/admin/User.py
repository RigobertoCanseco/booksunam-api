from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load
from v1.models.library.School import SchoolSchema


# DATA MODEL 'USER'
class User(db.Model):
    """
    Data Model: Table 'ADM_USERS'
    """
    __tablename__ = 'ADM_USERS'
    id = db.Column(db.String(32), primary_key=True, nullable=False, name="ID")
    school_id = db.Column(db.String(32), db.ForeignKey("LIB_SCHOOLS.ID"), nullable=False,  name="SCHOOL_ID")
    name = db.Column(db.String(256), nullable=False, name="NAME")
    lastname = db.Column(db.String(256), nullable=False, name="LASTNAME")
    genre = db.Column(db.String(16), nullable=False, name="GENRE")
    mail = db.Column(db.String(128), nullable=False, name="MAIL")
    password = db.Column(db.String(256), nullable=False, name="PASSWORD")
    account_number = db.Column(db.String(16), nullable=True, name="ACCOUNT_NUMBER")
    phone = db.Column(db.String(16), nullable=True, name="PHONE")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")

    # Relationships
    school = db.relationship("School", backref=db.backref("users", lazy="dynamic"))

    def __init__(self, school_id, name, lastname, genre, mail, password, account_number=0, phone=None,
                 active=True, status=0, type=0, creation_time=None, update_time=None):
        """
        
        :param school_id: 
        :param name: 
        :param lastname: 
        :param genre: 
        :param mail: 
        :param password: 
        :param account_number: 
        :param phone: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        self.id = KeysDB.create_id(mail)
        self.school_id = school_id
        self.name = name
        self.lastname = lastname
        self.genre = genre
        self.mail = mail
        self.password = KeysDB.password(password)
        self.account_number = account_number
        self.phone = phone
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<USER id='%s', school_id='%s', name='%s', lastname='%s',genre='%s', mail='%s', password='%s'," \
               " account_number='%s',  phone='%s', active='%s', status='%s', type='%s', creation_time='%s', " \
               "update_time='%s'>" \
               % (self.id, self.school_id,  self.name, self.lastname,  self.genre, self.mail, self.password,
                  self.account_number, self.phone, self.active, self.status, self.type, self.creation_time,
                  self.update_time)


# OBJECT MODEL 'USER'
class UserSchema(Schema):
    id = fields.Str()
    school_id = fields.Str()
    name = fields.Str()
    lastname = fields.Str()
    genre = fields.Str()
    mail = fields.Str()
    password = fields.Str()
    account_number = fields.Str()
    phone = fields.Str()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    school = fields.Nested(SchoolSchema)

    @post_load
    def make(self, data):
        return User(**data)
