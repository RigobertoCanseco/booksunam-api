# coding=utf-8
import datetime

from v1.models.library.Book import Book
from v1 import db
from v1.common.KeysDB import KeysDB
from marshmallow import Schema, fields, post_load, ValidationError
import re


INDEX = dict(
    title="titulo",
    thema="tema",
    author="autor",
    edition="imprenta",
    all="todos"
)

ORDER = dict(
    title="titulo",
    author="autor",
    classification="clasificacion"
)

BASE = dict(
    impress="LIBIMP", # book impress
    ebook="LIBDIG" # electronic book
)


# DATA MODEL 'NEW_BOOK'
class NewBook(db.Model):
    """
        Data Model: Table 'NEW_BOOK'
    """
    __tablename__ = 'NEW_BOOK'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    book_id = db.Column(db.String(32), db.ForeignKey("LIB_BOOKS.ID"), nullable=True, name="BOOK_ID")
    classification = db.Column(db.String(512), nullable=False, name="CLASSIFICATION")
    link_google_books = db.Column(db.String(512), nullable=False, name="LINK_GOOGLE_BOOKS")
    info_google = db.Column(db.String(512), nullable=False, name="INFO_GOOGLE")
    image = db.Column(db.String(512), nullable=False, name="IMAGE")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                            name="UPDATE_TIME")
    # RELATIONSHIP ONE TO MANY
    book = db.relationship("Book", backref=db.backref('news_books', lazy='dynamic'))

    def __init__(self, classification, link_google_books, info_google, image, book_id=None, active=True, status=0,
                 type=0, creation_time=None, update_time=None):
        """
        :param classification: 
        :param link_google_books: 
        :param info_google: 
        :param image: 
        :param book_id:  
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        self.id = KeysDB.create_id(classification.encode("utf-8"))
        self.book_id = book_id
        self.classification = classification
        self.link_google_books = link_google_books
        self.info_google = info_google
        self.image = image
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<Library id='%s', book_id='%s', classification='%s', link_google_books='%s', info_google='%s', " \
               "image='%s', active='%s', status='%s', type='%s', creation_time='%s', update_time='%s'>" % \
               (self.id, self.book_id, self.classification, self.link_google_books, self.info_google, self.image,
                self.active, self.status, self.type, self.creation_time, self.update_time)


def validate_base(v):
    if v not in BASE:
        raise ValidationError("Base of search not valid")


def validate_date(v):
    reg = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
    date = reg.search(v)

    if date is not None:
        try:
            date = datetime.datetime.strptime(date.group(), "%d/%m/%Y")
        except Exception as e:
            raise ValidationError("Format of date is invalid \"" + e.message + "\"")
    else:
        raise ValidationError("Format of date is invalid (Format valid='dd/mm/yyyy')")


def validate_term(v):
    if len(v) >= 64:
        raise ValidationError("Term of search not valid")


def validate_index(v):
    if v not in INDEX:
        raise ValidationError("Index of search not valid")


def validate_order(v):
    if v not in ORDER:
        raise ValidationError("Order of search not valid")


# OBJECT MODEL 'SEARCH_QUERY_SCHEMA'
class QueryNewBooksSchema(Schema):
    # KEY OF LIBRARY
    library = fields.Str(required = True)
    # DATE FROM
    date_from = fields.Str(required = True, validate = validate_date)
    # DATE TO
    date_to = fields.Str(required = True, validate = validate_date)
    # TYPE SEARCH
    base = fields.Str(required = True, validate = validate_base)
    term = fields.Str(defautl="", required = False, validate = validate_term)
    index = fields.Str(default = "title", required = False, validate = validate_index)
    order = fields.Str(default = "title", required = False, validate = validate_order)

    # AFTER OF FIND RESULTS
    init = fields.Str(required = False)
    total = fields.Str(required = False)

    def replace_values(self, data):

        data["date_from"] = datetime.datetime.strptime(data["date_from"], "%d/%m/%Y")
        data["date_to"] = datetime.datetime.strptime(data["date_to"], "%d/%m/%Y")
        if "term" in data:
            data["term"] = data['term'].encode('UTF-8')
        else:
            data["term"] = None

        if "index" in data:
            data["index"] = INDEX[data["index"]]
        else:
            data["index"] = "titulo"

        if "base" in data:
            data["base"] = BASE[data["base"]]

        if "order" in data:
            data["order"] = ORDER[data["order"]]
        else:
            data["order"] = "titulo"

        if "init" not in data:
            data["init"] = None

        if "total" not in data:
            data["total"] = None


# OBJECT MODEL 'NEW_BOOK'
class NewBookSchema(Schema):
    id = fields.Str()
    book_id = fields.Str()
    classification = fields.Str()
    link_google_books = fields.Str()
    info_google = fields.Str()
    image = fields.Str()
    active = fields.Bool()
    type = fields.Int()
    status = fields.Int()
    creation_time = fields.DateTime()
    update_time = fields.DateTime()
    parameters = fields.Nested(Book)

    @post_load
    def make(self, data):
        return NewBook(**data)


class NewBookItemSchema(Schema):
    id = fields.Str()
    classification = fields.Str()
    link_google_books = fields.Str()
    info_google = fields.Str()
    image = fields.Str()
    detail = fields.List(fields.Str())


class ResultSearchSchema(Schema):
    total = fields.Int(required = True, default = 0)
    books = fields.List(fields.Nested(NewBookItemSchema), required = True)
    next = fields.Str(allow_none = True)
    prev = fields.Str(required = False, allow_none = True)
