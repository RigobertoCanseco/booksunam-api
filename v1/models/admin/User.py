from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load, ValidationError, validate, pre_load, pre_dump, post_dump
from v1.models.library.School import SchoolSchema


GENRE = ["MALE", "FEMALE", "UNKNOWN", "OTHER"]


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

    def __init__(self, school_id, name, lastname, genre, mail, password, account_number=None, phone=None,
                 active=True, status=1, type=1, creation_time=None, update_time=None):
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


def validate_id(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'id' of user is invalid.")


def validate_school_id(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'school_id' of user is invalid.")


def validate_name(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'name' of user is invalid.")


def validate_lastname(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'lastname' of user is invalid.")


def validate_genre(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'genre' of user is invalid.")
    if v not in GENRE:
        raise ValidationError("Field 'genre' of user is invalid.")


def validate_mail(v):
    pass


def validate_pass(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'password' of user is invalid.")
    elif len(v) < 8:
        raise ValidationError("Field 'password' length minim is 8.")


def validate_account_number(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'account_number' of user is invalid.")
    elif len(v) > 16:
        raise ValidationError("Field 'account_number' of user is invalid.")


def validate_phone(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'phone' of user is invalid.")
    elif len(v) > 16:
        raise ValidationError("Field 'phone' of user is invalid.")


class LoginSchema(Schema):
    mail = fields.Str(required=True, validate = validate.Email(error="Field 'mail' of user is invalid."))
    password = fields.Str(required=True, validate = validate_pass)


# OBJECT MODEL 'USER'
class UserSchema(Schema):
    id = fields.Str(required=False)
    school_id = fields.Str(required=True, validate = validate_school_id)
    name = fields.Str(required=True, validate = validate_name)
    lastname = fields.Str(required=True, validate = validate_lastname)
    genre = fields.Str(required=True, validate = validate_genre)
    mail = fields.Str(required=True, validate = validate.Email(error="Field 'mail' of user is invalid."))
    password = fields.Str(required=True, validate = validate_pass)
    account_number = fields.Str(required=False, validate = validate_account_number)
    phone = fields.Str(required=False, validate = validate_phone)

    active = fields.Bool(required=False)
    status = fields.Int(required=False)
    type = fields.Int(required=False)
    creation_time = fields.DateTime(required=False)
    update_time = fields.DateTime(required = False)
    school = fields.Nested(SchoolSchema, required = False)

    @post_load
    def make(self, data):
        return User(**data)

    @pre_load
    def preload(self, data):
        if 'school_id' not in data:
            raise ValidationError("The object user must have a 'school_id' key.")

        if 'name' not in data:
            raise ValidationError("The object user must have a 'name' key.")
        else:
            data['name'] = data['name'].upper()

        if 'lastname' not in data:
            raise ValidationError("The object user must have a 'lastname' key.")
        else:
            data['lastname'] = data['lastname'].upper()

        if 'mail' not in data:
            raise ValidationError("The object user must have a 'mail' key.")

        if 'password' not in data:
            raise ValidationError("The object user must have a 'password' key.")

        if 'genre' not in data:
            raise ValidationError("The object user must have a 'genre' key.")
        else:
            data['genre'] = data['genre'].upper()

        # IGNORE
        if 'id' in data:
            del data['id']
        if 'active' in data:
            del data['active']
        if 'status' in data:
            del data['status']
        if 'type' in data:
            del data['type']
        if 'creation_time' in data:
            del data['creation_time']
        if 'update_time' in data:
            del data['update_time']

    @pre_dump
    def pre_dump(self, data):
        pass

    @post_dump
    def post_dump(self, data):
        pass
