from v1.flaskapp import db
import hashlib
import uuid


class BookFavorite(db.Model):
    """
    Data Model: Table 'LIB_BOOKS_FAVORITES'
    """
    __tablename__ = 'LIB_BOOKS_FAVORITES'
    book_id = db.Column(db.String(32), db.ForeignKey("LIB__BOOKS.ID"), primary_key=True, name="BOOK_ID")
    user_id = db.Column(db.String(32), db.ForeignKey("ADM_USERS.ID"), primary_key=True, name="USER_ID")
    last_sync =  db.Column(db.DateTime, default=db.func.current_timestamp(), name="LAST_SYNC")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                name="UPDATE_TIME")

    # Relationships
    book = db.relationship("LIB_BOOKS", backref=db.backref('books', lazy='dynamic'))
    user = db.relationship("ADM_USERS", backref=db.backref('users', lazy='dynamic'))


    def __init__(self, book_id, user_id, last_sync=None, active=True, status=0, type=0, creation_time=None,
                 update_time=None):
        """
        
        :param book_id: 
        :param user_id: 
        :param last_sync: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        self.book_id = book_id
        self.user_id = user_id
        self.last_sync = last_sync
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "<BookFavorite book_id_id='%s', user_id='%s', last_sync='%s', active='%s', status='%s', type='%s', " \
               "creation_time='%s', update_time='%s'>" % \
               (self.book_id, self.user_id, self.last_sync, self.active, self.status, self.type, self.creation_time,
                self.update_time )

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
