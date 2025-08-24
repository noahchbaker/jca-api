# used https://medium.com/@iambkpl/setup-fastapi-and-sqlalchemy-mysql-986419dbffeb as reference

import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
import models
from database import SessionLocal, engine


# run INIT_DB=1 uvicorn main:app --reload if you want to remake tables
if os.getenv("INIT_DB") == "1":
    models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

'''
@app.post("/students/{student_id}/schedule/",response_model=schemas.Schedule)
def post_todo_for_user(user_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
    return crud.create_user_todo(db=db,user_id=user_id, todo=todo)


@app.get("/schedule/", response_model=list[schemas.Schedule])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = crud.get_todos(db,skip=skip,limit=limit)
    return todos
'''