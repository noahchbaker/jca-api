from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

'''
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),index=True)
    email = Column(String(255), unique=True, index=True)
    todos = relationship("Todo",back_populates="owner")
    is_active = Column(Boolean,default=False)



class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User",back_populates="todos")
'''

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),index=True)
    email = Column(String(255), unique=True, index=True)
    major_id = Column(Integer, ForeignKey("major.id"))
    app_entry_term = Column(Integer, index = True)
    mst_rec_desc = Column(String(255),index=True)

class Event(Base):
    __tablename__ = "event"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255),index=True)
    building_id = Column(Integer, ForeignKey("building.id"))
    day_id = Column(Integer, ForeignKey("days.id"))
    time_start = Column(Integer, ForeignKey("hour.id"))
    time_end = Column(Integer, ForeignKey("hour.id"))

class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    event_id = Column(Integer, ForeignKey("event.id"))

class Major(Base):
    __tablename__ = "major"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255),index=True)
    notes = Column(String(255), index=True, nullable=True)

class Building(Base):
    __tablename__ = "building"
    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(255),index=True)
    Room = Column(String(255),index=True)
    Capacity = Column(Integer,index=True)

class Hour(Base):
    __tablename__ = "hour"
    id = Column(Integer,primary_key=True,index=True)
    time = Column(String(255),index=True)

class Days(Base):
    __tablename__ = "days"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255),index=True)