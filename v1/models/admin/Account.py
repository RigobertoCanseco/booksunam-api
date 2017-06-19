from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load
from v1.models.admin.User import UserSchema
from v1.models.library.Library import LibrarySchema


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
    user = db.relationship("User", backref=db.backref("accounts", lazy="dynamic"))
    library = db.relationship("Library", backref=db.backref("accounts", lazy="dynamic"))

    def __init__(self, user_id, library_id, account, password, active=True, status=0, type=0, creation_time=None,
                 update_time=None):
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

    def __repr__(self):
        return "<Account(id='%s', user_id='%s', library_id='%s', account='%s', password='%s', active='%s', " \
               "status='%s', type='%s', creation_time='%s', update_time='%s')>" \
               % (self.id, self.user_id, self.library_id, self.account, self.password, self.active, self.status,
                  self.type, self.creation_time, self.update_time)


# OBJECT MODEL 'ACCOUNT'
class AccountSchema(Schema):
    id = fields.Str()
    user_id = fields.Str()
    library_id = fields.Str()
    account = fields.Str()
    password = fields.Str()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    user = fields.Nested(UserSchema)
    library = fields.Nested(LibrarySchema)

    @post_load
    def make(self, data):
        return Account(**data)
