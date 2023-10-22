from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from datetime import date, time

from src.database import get_db
from . import models, schemas, service
from src.barbers import service as barber_service

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    print(appointment)
    appointment_taken = service.get_by_barber_id_on_datetime(db=db, barber_id=appointment.barber_id,
                                                                    appointment_date=appointment.appointment_date,
                                                                    appointment_time=appointment.appointment_time)
    if appointment_taken:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Barber is busy at that time.")
    
    return service.create(db=db, appointment=appointment)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.Appointment])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = service.get_all(db=db, skip=skip, limit=limit)
    return appointments

@router.get("/{barber_id}", status_code=status.HTTP_200_OK, response_model=list[schemas.Appointment])
def get_appointments_by_barber_id(barber_id: int, db: Session = Depends(get_db)):
    appointments = service.get_by_barber_id(db=db, barber_id=barber_id)
    if not appointments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no appointments")
    return appointments


@router.get("/{barber_id}/{appointment_date}", status_code=status.HTTP_200_OK, response_model=list[schemas.Appointment])
def get_busy_hours_by_barber_id_on_date(barber_id: int, appointment_date: str, db: Session = Depends(get_db)):
    appointments = service.get_by_barber_id_on_date(db=db, barber_id=barber_id, appointment_date=appointment_date)
    # if not appointments:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no appointments")
    return appointments



@router.get("/{barber_id}/{appointment_date}/{appointment_time}", status_code=status.HTTP_200_OK, response_model=schemas.Appointment)
def get_appointment_by_barber_id_on_datetime(barber_id: int, appointment_date: str, appointment_time: str, db: Session = Depends(get_db)):
    appointment = service.get_by_barber_id_on_datetime(db=db, barber_id=barber_id, appointment_date=appointment_date, appointment_time=appointment_time)
    if not appointment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found.")
    return appointment