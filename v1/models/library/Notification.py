from v1 import db
import hashlib
import uuid


class Notification(db.Model):
    """
    Data Model: Table 'LIB_NOTIFICATIONS'
    """
    __tablename__ = 'LIB_NOTIFICATIONS'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    device_id = db.Column(db.String(32), db.ForeignKey("ADM_DEVICES.ID"), nullable=False, name="DEVICE_ID")
    borrow_book_id = db.Column(db.String(32), db.ForeignKey("LIB_BORROW_BOOKS.ID"), nullable=False, name="BORROW_BOOK_ID")
    last_notification_time = db.Column(db.DateTime, nullable=True, name="LAST_NOTIFICATION_TIME")
    next_notification_time = db.Column(db.DateTime, nullable=True, name="NEXT_NOTIFICATION_TIME")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                name="UPDATE_TIME")

    # Relationships
    device = db.relationship("ADM_DEVICES", backref=db.backref('devices', lazy='dynamic'))
    borrow_book = db.relationship("LIB_BORROW_BOOKS", backref=db.backref('borrow_books', lazy='dynamic'))


    def __init__(self, device_id, borrow_book_id, id=None, last_notification_time=None, next_notification_time=None,
                active=True, status=0, type=0, creation_time=None, update_time=None):
        """
        
        :param device_id: 
        :param borrow_book_id: 
        :param id: 
        :param last_notification_time: 
        :param next_notification_time: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        if id is None:
            self.id = self.__create_id__(device_id + borrow_book_id)
        else:
            self.id = id

        self.device_id = device_id
        self.borrow_book_id = borrow_book_id
        self.last_notification_time = last_notification_time
        self.next_notification_time = next_notification_time
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "Notifications"

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
