from pydantic import BaseModel
from typing import List, Optional


class BaseSchedule(BaseModel):
    student_id: int
    event_id: int

class ScheduleCreate(BaseSchedule):
    pass

class Schedule(BaseSchedule):
    id: int

    class Config:
        orm_mode = True


class BaseStudent(BaseModel):
    name: str
    email: str
    major_id: int
    app_entry_term: int
    mst_rec_desc: Optional[str] = None

class StudentCreate(BaseStudent):
    pass 

class Student(BaseStudent):
    id: int
    #schedule: List[Schedule] = []

    class Config:
        orm_mode = True


class BaseEvent(BaseModel):
    title: str
    building_id: int
    day_id: int
    time_start: int
    time_end: int

class CreateEvent(BaseEvent):
    pass 

class Event(BaseEvent):
    id: int

    class Config:
        orm_mode = True


class BaseMajor(BaseModel):
    title: str
    notes: Optional[str] = None

class CreateMajor(BaseMajor):
    pass

class Major(BaseMajor):
    id: int

    class Config:
        orm_mode = True
    

class BaseBuilding(BaseModel):
    Name: str
    Room: str
    Capacity: int

class CreateBuilding(BaseBuilding):
    pass 

class Building(BaseBuilding):
    id: int

    class Config:
        orm_mode = True

class BaseHour(BaseModel):
    time: str

class CreateHour(BaseHour):
    pass 

class Hour(BaseHour):
    id: int

    class Config:
        orm_mode = True

class BaseDays(BaseModel):
    title: str

class CreateDay(BaseDays):
    pass 

class Days(BaseDays):
    id: int

    class Config:
        orm_mode = True