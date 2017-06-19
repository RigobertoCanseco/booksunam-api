from marshmallow import Schema, fields, post_load
from v1 import db
from v1.common.KeysDB import KeysDB
from v1.models.library.Library import LibrarySchema


# DATA MODEL 'BOOK'
class Book(db.Model):
    """
    Data Model: Table 'LIB_BOOKS'
    """
    __tablename__ = 'LIB_BOOKS'
    id = db.Column(db.String(32), primary_key=True, nullable=False, name="ID")
    library_id = db.Column(db.String(32), db.ForeignKey("LIB_LIBRARY.ID"), nullable=False, name="LIBRARY_ID")
    author = db.Column(db.String(128), nullable=False, name="AUTHOR")
    title = db.Column(db.String(256), nullable=False, name="TITLE")
    year = db.Column(db.String(8), nullable=False, name="YEAR")
    number_system = db.Column(db.String(32), nullable=False, name="NUMBER_SYSTEM")
    classification = db.Column(db.String(64), nullable=False, name="CLASSIFICATION")
    classification_dewey = db.Column(db.String(64), nullable=True, name="CLASSIFICATION_DEWEY")
    isbn = db.Column(db.String(64), nullable=False, name="ISBN")
    total = db.Column(db.Integer, nullable=False, name="TOTAL")
    exemplary = db.Column(db.Integer, nullable=False, name="EXEMPLARY")
    taken = db.Column(db.Integer, nullable=False, name="TAKEN")
    publication_data = db.Column(db.String(128), nullable=True, name="PUBLICATION_DATA")
    description = db.Column(db.String(256), nullable=True, name="DESCRIPTION")
    serie = db.Column(db.String(256), nullable=True, name="SERIE")
    courses = db.Column(db.String(256), nullable=True, name="COURSES")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")
    # Relationships
    library = db.relationship("Library", backref=db.backref('books', lazy='dynamic'))

    def __init__(self, library_id, title, author, classification, isbn, year, number_system, total,
                 exemplary, taken, classification_dewey=None, publication_data=None, description=None, serie=None,
                 courses=None, type=0, active=True, status=0, creation_time=None, update_time=None):
        self.id = KeysDB.create_id(library_id+classification)
        self.library_id = library_id
        self.title = title
        self.author = author
        self.classification = classification
        self.isbn = isbn
        self.year = year
        self.number_system = number_system
        self.total = total
        self. classification_dewey = classification_dewey
        self.exemplary = exemplary
        self.taken = taken
        self.publication_data = publication_data
        self.description = description
        self.serie = serie
        self.courses = courses
        self.type = type
        self.active = active
        self.status = status
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<Book(id='%s', library_id='%s', title='%s')>" % (self.id, self.library_id, self.title)


# OBJECT MODEL 'BOOK'
class BookSchema(Schema):
    id = fields.Str()
    library_id = fields.Str()
    title = fields.Str()
    author = fields.Str()
    classification = fields.Str()
    isbn = fields.Str()
    year = fields.Str()
    number_system = fields.Str()
    classification_dewey = fields.Str()
    total = fields.Int()
    exemplary = fields.Int()
    taken = fields.Int()
    publication_data = fields.Str()
    description = fields.Str()
    serie = fields.Str()
    courses = fields.Str()
    active = fields.Bool()
    status = fields.Int()
    type = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    library = fields.Nested(LibrarySchema)


    @post_load
    def make(self, data):
        return Book(**data)
