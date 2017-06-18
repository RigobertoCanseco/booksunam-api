from v1.flaskapp import db
import hashlib
import uuid


class BorrowBook(db.Model):
    """
    Data Model: Table 'LIB_BORROW_BOOKS'
    """
    __tablename__ = 'LIB_BORROW_BOOKS'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    book_id = db.Column(db.String(32), db.ForeignKey("LIB_BOOKS.ID"), name="BOOK_ID")
    user_id = db.Column(db.String(32), db.ForeignKey("ADM_USERS.ID"), name="USER_ID")
    take_time = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False, name="TAKE_TIME")
    expiration_time = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False, name="EXPIRATION_TIME")
    renovations = db.Column(db.Integer, nullable=False, default=0, name="RENOVATIONS")
    mulct = db.Column(db.Integer, nullable=False, default=0, name="MULCT")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                name="UPDATE_TIME")

    # Relationships
    book = db.relationship("LIB_BOOKS", backref=db.backref('books', lazy='dynamic'))
    user = db.relationship("ADM_USERS", backref=db.backref('users', lazy='dynamic'))


    def __init__(self, book_id, user_id, take_time, expiration_time, renovations=0, mulct=0, id=None, active=True,
                 status=0, type=0, creation_time=None, update_time=None):
        """
        
        :param book_id: 
        :param user_id: 
        :param take_time: 
        :param expiration_time: 
        :param renovations: 
        :param mulct:
        :param id:
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        if id is None:
            self.id = self.__create_id__(book_id+user_id+take_time)
        else:
            self.id = id
        self.book_id = book_id
        self.user_id = user_id
        self.take_time = take_time
        self.expiration_time = expiration_time
        self.renovations = renovations
        self.mulct = mulct
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<BorrowBook id='%s', book_id='%s', user_id='%s', take_time='%s', expiration_time='%s', renovations='%s', " \
               "mulct='%s', active='%s', status='%s', type='%s', creation_time='%s', update_time='%s'>" % \
               (self.id, self.book_id, self.user_id, self.take_time, self.expiration_time, self.renovations,
                self.mulct, self.active, self.status, self.type, self.creation_time, self.update_time )

    def __create_id__(self, id):
        """
        Create md5 to id
        :param id: 
        :return: md5(id)
        """
        return hashlib.md5(id).hexdigest()

    def __pass__(self, password):
        """
        Create SHA to password
        :param password:
        :return: sha256
        """
        return hashlib.sha256(password).hexdigest()

    def __uuid__(self):
        """
        Create UUID
        :return: UUID 
        """
        return uuid.uuid1()
