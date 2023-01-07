from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DataBase import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, index=False)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todos = relationship("Todos", back_populates="owner")


class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, nullable=False)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)

    owner = relationship('User', back_populates="todos")