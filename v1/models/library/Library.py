# coding=utf-8
from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load


# DATA MODEL 'LIBRARY'
class Library(db.Model):
    """
        Data Model: Table 'ADM_LIBRARY'
    """
    __tablename__ = 'LIB_LIBRARY'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    class_name = db.Column(db.String(32), unique=True, nullable=False, name="CLASS_NAME")
    name = db.Column(db.String(64), unique=False, nullable=False, name="NAME")
    division = db.Column(db.String(128), nullable=False,  name="DIVISION")
    entity = db.Column(db.String(128), nullable=False, name="ENTITY")
    website = db.Column(db.String(128), nullable=False, name="WEBSITE")
    address = db.Column(db.String(256), nullable=False, name="ADDRESS")
    telephone = db.Column(db.String(64), nullable=False, name="TELEPHONE")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")
    # RELATIONSHIP ONE TO MANY
    # parameters = relationship("LIB_LIBRARY_PARAMETERS",  back_populates="library")
    parameters = db.relationship("LibraryParameter")

    def __init__(self, class_name, name, division, entity, website, address, telephone, id=None, active=True, status=0,
                 type=0, creation_time=None, update_time=None, parameters=None):
        """
        :param class_name:
        :param name: 
        :param division: 
        :param entity: 
        :param website: 
        :param address: 
        :param telephone: 
        :param id: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        :param parameters:
        """
        self.id = KeysDB.create_id(division.encode("utf-8") + entity.encode("utf-8"))
        self.class_name = class_name
        self.entity = entity
        self.division = division
        self.name = name
        self.website = website
        self.address = address
        self.telephone = telephone
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time
        self.parameters = parameters

    def __repr__(self):
        return "<Library id='%s', class_name='%s', name='%s', division='%s', entity='%s', website='%s', address='%s', "\
               "telephone='%s', active='%s', status='%s', type='%s', creation_time='%s', update_time='%s', " \
               "parameters='%s'>" % \
               (self.id, self.class_name, self.name, self.division, self.entity, self.website, self.address,
                self.telephone, self.active, self.status, self.type, self.creation_time, self.update_time,
                self.parameters)


# DATA MODEL 'LIBRARY_PARAMETERS'
class LibraryParameter(db.Model):
    """
    Data Model: Table 'LIB_LIBRARY_PARAMETERS'
    """
    __tablename__ = 'LIB_LIBRARY_PARAMETERS'
    id = db.Column(db.String(32), db.ForeignKey("LIB_LIBRARY.ID"), primary_key=True, name="ID")
    field = db.Column(db.String(64), primary_key=True, nullable=False, name="FIELD")
    parameter = db.Column(db.String(64), nullable=False, name="PARAMETER")
    value = db.Column(db.String(1024), nullable=False, name="VALUE")

    # Relationships
    # "library = db.relationship("Library", back_populates="parameters")
    # parameters = db.relationship("Library", backref=db.backref('library', lazy='dynamic'))

    def __init__(self, field, parameter, value, id=None, library=None):
        """

        :param id: 
        :param field: 
        :param parameter: 
        :param value: 
        """
        self.id = id
        self.field = field
        self.parameter = parameter
        self.value = value
        self.library = library

    def __repr__(self):
        return "<LibraryParameter id='%s', field='%s', parameter='%s', value='%s', library='%s'>" % \
               (self.id, self.field, self.parameter, self.value, self.library)


# OBJECT MODEL 'LIBRARY_PARAMETERS'
class LibraryParametersSchema(Schema):
    id = fields.Str()
    parameter = fields.Str()
    field = fields.Str()
    value = fields.Str()

    @post_load
    def make_parameters(self, data):
        return LibraryParameter(**data)


# OBJECT MODEL 'LIBRARY'
class LibrarySchema(Schema):
    id = fields.Str()
    class_name = fields.Str()
    name = fields.Str()
    division = fields.Str()
    entity = fields.Str()
    website = fields.Str()
    address = fields.Str()
    telephone = fields.Str()
    active = fields.Bool()
    type = fields.Int()
    status = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    parameters = fields.List(fields.Nested(LibraryParametersSchema))

    @post_load
    def make_user(self, data):
        return Library(**data)
