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