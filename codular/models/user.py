from .meta import (Base, DBSession)

from sqlalchemy.orm import (
    synonym,
)

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode
    )

import cryptacular.bcrypt

crypt = cryptacular.bcrypt.BCRYPTPasswordManager()

"""
Return a unicode hash of the password, using BCrypt from cryptacular
"""
def hash_password(password):
    return str(crypt.encode(password))

class User(Base):
    """
    User model
    """
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(Unicode(20), unique=True)
    name = Column(Unicode(50))
    email = Column(Unicode(50))

    _password = Column('password', Unicode(60))

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = hash_password(password)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, username, password, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def get_by_username(cls, username):
        return DBSession.query(cls).filter(cls.username == username).first

    @classmethod
    def check_password(cls, username, password):
        user = cls.get_by_username(username)
        if not user:
            return False
        return crypt.check(user.password, password)
