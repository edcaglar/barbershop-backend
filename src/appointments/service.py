from sqlalchemy.orm import Session
from datetime import datetime, date, time
from fastapi import HTTPException

from . import models, schemas
from src.barbers import service as barber_service

def get(db:Session, id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def create(db: Session, appointment: schemas.AppointmentCreate):
    barber = barber_service.get(db=db, id=appointment.barber_id)
    if not barber:
        raise HTTPException(status_code=404, detail="Barber not found.")
    new_appointment = models.Appointment(**appointment.model_dump())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)
    return new_appointment


def get_by_credentials(db: Session, customer_surname: str, customer_phone: str):
    appointments = db.query(models.Appointment).filter(models.Appointment.customer_surname == customer_surname,
                                                       models.Appointment.customer_phone == customer_phone).all()
    if not appointments:
        raise HTTPException(status_code=404, detail="Appointment not found.")
    return appointments

def get_by_barber_id(db: Session, barber_id: int):
    appointments = db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id).all()
    if not appointments:
        raise HTTPException(status_code=404, detail="There is no appointments.")
    return appointments

def get_by_barber_id_on_date(db: Session, barber_id: int, appointment_date: date):
    appointments = db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id,
                                               models.Appointment.appointment_date == appointment_date).all()
    if not appointments:
        raise HTTPException(status_code=404, detail="There is no appointments.")
    return appointments

def get_by_barber_id_on_datetime(db: Session, barber_id: int, appointment_date: date, appointment_time: str):
    appointments = db.query(models.Appointment).filter(models.Appointment.barber_id == barber_id,
                                               models.Appointment.appointment_date == appointment_date,
                                               models.Appointment.appointment_time == appointment_time).first()
    if not appointments:
        raise HTTPException(status_code=404, detail="There is no appointments.")
    return appointments



    