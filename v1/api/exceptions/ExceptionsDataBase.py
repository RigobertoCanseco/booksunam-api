from sqlalchemy.exc import *


class ExceptionsDataBase:
    """
    
    """

    def __init__(self, e=SQLAlchemyError):
        """
        :param e: 
        """
        if e is IntegrityError:
            print "IntegrityError"
            self.code = 409
        elif e is OperationalError:
            print "OperationalError:"
            self.code = 409
        else:
            print "SQLAlchemyError:"
        print e.message

    def get_code(self):
        return self.code
