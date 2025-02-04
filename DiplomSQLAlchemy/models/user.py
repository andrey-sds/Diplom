from sqlalchemy import Table, Column, Integer, String
from backend.db import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
