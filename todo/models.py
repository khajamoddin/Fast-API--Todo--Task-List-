from sqlalchemy import Column, Integer, String, ForeignKey
from todo.database import Base
from sqlalchemy.orm import relationship

class Todo(Base):
    __tablename__ = 'Tasks'

    id = Column(Integer, primary_key=True, index=True)
    tasks = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="Tasks")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    tasks = relationship('Tasks', back_populates="creator")