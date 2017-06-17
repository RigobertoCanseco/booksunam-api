import hashlib
import uuid


class KeysDB:
    def __init__(self):
        pass

    @staticmethod
    def create_id(id):
        """
        Create md5 to id
        :param id: 
        :return: md5(id)
        """
        return hashlib.md5(id).hexdigest()

    @staticmethod
    def password(password):
        """
        Create SHA to password
        :param password:
        :return: sha256
        """
        return hashlib.sha256(password).hexdigest()

    @staticmethod
    def uuid():
        """
        Create UUID
        :return: UUID 
        """
        return uuid.uuid1()
