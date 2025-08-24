from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel
import sqlalchemy

class Student(BaseModel):
    student_id: int
    name: str
    email: str
    major_id: int
    app_entry_term: int
    mst_rec_desc: int

class Event(BaseModel):
    event_id: int
    title: str
    building_id: int
    day_id: int
    time_start: int
    time_end: int

class Schedule(BaseModel):
    schedule_id: int
    student_id: int
    event_id: int

class Major(BaseModel):
    major_id: int
    title: str
    instrument: str
    notes: str

class Building(BaseModel):
    building_id: int
    Name: str
    Room: str
    Capacity: int

class Hour(BaseModel):
    hour_id: int
    time: str

class Days(BaseModel):
    days_id: int
    title: str

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://ncbaker:Jordan5744!!@192.168.50.108:3306/audition")


def get_session():
    with Session(engine) as session:
        yield session

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/student/{student_id}")
def read_student(student_id: int,):
    return {"student_id" : student_id}


@app.put("/student/{student_id}")
def update_item(student_id: int, student: Student):
    return {"student_id": student_id, **student.model_dump()}

@app.post("/student/")
def create_student(student: Student) -> Student:
    return student
