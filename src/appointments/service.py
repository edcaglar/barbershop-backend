from sqlalchemy.orm import Session
from datetime import datetime, date, time
from fastapi import HTTPException

from src.barbers import models as barber_models
from . import models, schemas

def get(db:Session, id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def create(db: Session, appointment: schemas.AppointmentCreate):
    new_appointment = models.Appointment(**appointment.model_dump())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment


def get_by_credentials(db: Session, customer_surname: str, customer_phone: str):
    return db.query(models.Appointment).filter(models.Appointment.customer_surname == customer_surname,
                                                       models.Appointment.customer_phone == customer_phone).all()


def get_by_barber_id(db: Session, barber_id: int):
    return db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id).all()

def get_by_username(db: Session, username: str):
    barber = db.query(barber_models.Barber).filter(barber_models.Barber.username == username).first()
    barber_id = barber.id
    return db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id).all()

def get_by_username_on_date(db: Session, username: str, appointment_date: str):
    barber = db.query(barber_models.Barber).filter(barber_models.Barber.username == username).first()
    print("z")
    return db.query(models.Appointment).filter(models.Appointment.barber_id == barber.id,
                                               models.Appointment.appointment_date == appointment_date).all()

def get_by_barber_id_on_date(db: Session, barber_id: int, appointment_date: str):
    return db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id,
                                               models.Appointment.appointment_date == appointment_date).all()

def get_by_barber_id_on_datetime(db: Session, barber_id: int, appointment_date: str, appointment_time: str):
    return db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id,
                                               models.Appointment.appointment_date == appointment_date,
                                               models.Appointment.appointment_time == appointment_time).first()




    