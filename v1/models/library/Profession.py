from v1.flaskapp import db
import hashlib
import uuid


class Profession(db.Model):
    """
    Data Model: Table 'LIB_PROFESSIONS'
    """
    __tablename__ = 'LIB_PROFESSIONS'
    id = db.Column(db.String(32), primary_key=True, name="ID")
    school_id = db.Column(db.String(32), db.ForeignKey("LIB_SCHOOLS.ID"), name="SCHOOL_ID")
    profession = db.Column(db.String(64), nullable=False, name="PROFESSION")
    active = db.Column(db.Boolean, nullable=False, default=True, name="ACTIVE")
    status = db.Column(db.Integer, nullable=False, default=0, name="STATUS")
    type = db.Column(db.Integer, nullable=False, default=0, name="TYPE")
    creation_time = db.Column(db.DateTime, default=db.func.current_timestamp(), name="CREATION_TIME")
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),
                name="UPDATE_TIME")

    # Relationships
    school = db.relationship("LIB_SCHOOLS", backref=db.backref('schools', lazy='dynamic'))


    def __init__(self, school_id, profession,active=True, status=0, type=0, creation_time=None, update_time=None):
        """
        
        :param school_id: 
        :param profession: 
        :param id: 
        :param active: 
        :param status: 
        :param type: 
        :param creation_time: 
        :param update_time: 
        """
        self.id = self.__create_id__(school_id+profession)

        self.school_id = school_id
        self.profession = profession
        self.active = active
        self.status = status
        self.type = type
        self.creation_time = creation_time
        self.update_time = update_time

    def __repr__(self):
        return "Professions"

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
