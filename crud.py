from sqlalchemy.orm import Session

import schemas

import models


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()


def get_students(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student(db: Session, student:schemas.StudentCreate):
    db_student = models.Student(name = student.name,
                          email = student.email,
                          major_id = student.major_id,
                          app_entry_term = student.app_entry_term,
                          mst_rec_desc = student.mst_rec_desc)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_major(db: Session, major:schemas.CreateMajor):
    db_major = models.Major(title = major.title)
    db.add(db_major)
    db.commit()
    db.refresh(db_major)
    return db_major

def get_majors(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Major).offset(skip).limit(limit).all()


def create_event(db: Session, event:schemas.CreateEvent):
    db_event = models.Event(title = event.title,
                          building_id = event.building_id,
                          day_id = event.day_id,
                          time_start = event.time_start,
                          time_end = event.time_end)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Event).offset(skip).limit(limit).all()


def create_day(db: Session, day:schemas.CreateDay):
    db_day = models.Event(title = day.title)
    db.add(db_day)
    db.commit()
    db.refresh(db_day)
    return db_day

def get_days(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Days).offset(skip).limit(limit).all()

def create_hour(db: Session, hour:schemas.CreateHour):
    db_hour = models.Hour(time = hour.time)
    db.add(db_hour)
    db.commit()
    db.refresh(db_hour)
    return db_hour

def get_hours(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Hour).offset(skip).limit(limit).all()

def create_building(db: Session, building:schemas.CreateBuilding):
    db_event = models.Building(name = building.name,
                          room = building.room,
                          capacity = building.capacity)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_building(db: Session, skip:int=0, limit:int=100):
    return db.query(models.Building).offset(skip).limit(limit).all()