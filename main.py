# used https://medium.com/@iambkpl/setup-fastapi-and-sqlalchemy-mysql-986419dbffeb as reference

import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
import models
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware



# run INIT_DB=1 uvicorn main:app --reload if you want to remake tables
if os.getenv("INIT_DB") == "1":
    models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.50.199:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()


@app.post("/student/", response_model=schemas.Student)
def post_user(student:schemas.StudentCreate, db:Session=Depends(get_db)):
    db_student = crud.get_student_by_email(db, email=student.email)
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_student(db=db,student=student)


@app.get("/student/", response_model=list[schemas.Student])
def get_students(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    students = crud.get_students(db,skip=skip,limit=limit)
    return students


@app.get("/student/{student_id}/",response_model=schemas.Student)
def get_student(student_id:int, db:Session=Depends(get_db)):
    db_student = crud.get_student(db,student_id = student_id )
    if not db_student:
        raise HTTPException(status_code=404, detail="User not found")
    return db_student

@app.post("/major/", response_model=schemas.Major)
def post_user(major:schemas.CreateMajor, db:Session=Depends(get_db)):
    return crud.create_major(db=db,major=major)

@app.get("/major/", response_model=list[schemas.Major])
def get_majors(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    majors = crud.get_majors(db,skip=skip,limit=limit)
    return majors

@app.post("/event/", response_model=schemas.Event)
def post_event(event:schemas.CreateEvent, db:Session=Depends(get_db)):
    return crud.create_event(db=db,event=event)

@app.get("/event/", response_model=list[schemas.Event])
def get_events(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    events = crud.get_events(db,skip=skip,limit=limit)
    return events

@app.post("/days/", response_model=schemas.Days)
def post_day(day:schemas.CreateDay, db:Session=Depends(get_db)):
    return crud.create_day(db=db,days=day)

@app.get("/days/", response_model=list[schemas.Days])
def get_days(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    days = crud.get_days(db,skip=skip,limit=limit)
    return days

@app.post("/hour/", response_model=schemas.Hour)
def post_hour(hour:schemas.CreateHour, db:Session=Depends(get_db)):
    return crud.create_hour(db=db,hour=hour)

@app.get("/hour/", response_model=list[schemas.Event])
def get_hours(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    hours = crud.get_hours(db,skip=skip,limit=limit)
    return hours

@app.post("/building/", response_model=schemas.Event)
def post_building(building:schemas.CreateBuilding, db:Session=Depends(get_db)):
    return crud.create_building(db=db,building=building)

@app.get("/building/", response_model=list[schemas.Event])
def get_buildings(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    buildings = crud.get_building(db,skip=skip,limit=limit)
    return buildings

'''
@app.post("/students/{student_id}/schedule/",response_model=schemas.Schedule)
def post_todo_for_user(user_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
    return crud.create_user_todo(db=db,user_id=user_id, todo=todo)


@app.get("/schedule/", response_model=list[schemas.Schedule])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = crud.get_todos(db,skip=skip,limit=limit)
    return todos
'''