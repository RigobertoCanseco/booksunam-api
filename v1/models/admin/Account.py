from v1.models.library.Library import LibrarySchema
from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load, ValidationError, pre_load, pre_dump, post_dump


# DATA MODEL 'ACCOUNT'
class Account(db.Model):
    """
    Data Model: Table 'ADM_ACCOUNTS'
    """
    __tablename__ = 'ADM_ACCOUNTS'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    user_id = db.Column(db.String(32), db.ForeignKey('ADM_USERS.ID'), nullable=False, name="USER_ID")
    library_id = db.Column(db.String(32), db.ForeignKey('LIB_LIBRARY.ID'),  nullable=False, name="LIBRARY_ID")
    account = db.Column(db.String(32), nullable=False, name="ACCOUNT")
    password = db.Column(db.String(32), nullable=False, name="PASSWORD")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")

    # Relationships
    # user = db.relationship("User", backref=db.backref("accounts", lazy="dynamic"))
    library = db.relationship("Library", backref=db.backref("accounts", lazy="dynamic"))

    def __init__(self, user_id, library_id, account, password, active=True, status=0, type=0, creation_time=None,
                 update_time=None, user=None):
        """
        :param user_id:
        :param library_id: 
        :param account: 
        :param password: 
        :param creation_time: 
        :param update_time: 
        :param status: 
        :param active: 
        :param type: 
        """
        self.id = KeysDB.create_id(user_id + library_id)
        self.user_id = user_id
        self.library_id = library_id
        self.account = account
        self.password = KeysDB.password(password)
        self.creation_time = creation_time
        self.update_time = update_time
        self.status = status
        self.active = active
        self.type = type
        self.user = user

    def __repr__(self):
        return "<Account(id='%s', user_id='%s', library_id='%s', account='%s', password='%s', active='%s', " \
               "status='%s', type='%s', creation_time='%s', update_time='%s', user='%s')>" \
               % (self.id, self.user_id, self.library_id, self.account, self.password, self.active, self.status,
                  self.type, self.creation_time, self.update_time, self.user)


def validate_user_id(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'user_id' of user is invalid.")


def validate_library_id(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'library_id' of user is invalid.")


def validate_account(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'account' of user is invalid.")
    elif len(v) > 16:
        raise ValidationError("Field 'account' of user is invalid.")


def validate_pass(v):
    if type(v) is not unicode:
        raise ValidationError("Field 'password' of user is invalid.")
    elif len(v) < 4:
        raise ValidationError("Field 'password' length minim is 8.")


# OBJECT MODEL 'ACCOUNT'
class AccountSchema(Schema):
    id = fields.Str(required = False)
    user_id = fields.Str(required = True, validate = validate_user_id)
    library_id = fields.Str(required = True, validate = validate_library_id)
    account = fields.Str(required = True, validate = validate_account)
    password = fields.Str(required = True, validate = validate_pass)

    active = fields.Bool(required = False)
    status = fields.Int(required = False)
    type = fields.Int(required = False)
    creation_time = fields.DateTime(required = False)
    update_time = fields.DateTime(required = False)
    # user = fields.Nested(UserSchema, required = False)
    library = fields.Nested(LibrarySchema, required = False)

    @post_load
    def make(self, data):
        return Account(**data)

    @pre_load
    def preload(self, data):
        if 'user_id' not in data:
            raise ValidationError("The object 'Account' must have a 'user_id' key.")

        if 'library_id' not in data:
            raise ValidationError("The object 'Account' must have a 'library_id' key.")

        if 'account' not in data:
            raise ValidationError("The object 'Account' must have a 'account' key.")

        if 'password' not in data:
            raise ValidationError("The object 'Account' must have a 'password' key.")

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
