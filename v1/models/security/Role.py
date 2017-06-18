from v1.flaskapp import db


class Role(db.Model):
    """
    Data Model: Table 'ADM_ROLES'
    """
    __tablename__ = 'ADM_ROLES'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, name="ID")
    role = db.Column(db.String(45), nullable=False, unique=True, name="ROLE")

    def __init__(self, id=int, role=str):
        """
        :param id: 
        :param role: 
        """
        self.id = id
        self.role = role

    def __repr__(self):
        return '<Role %r>' % (self.role)