from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from src.database import get_db

from src.auth.config import auth_config
from src.auth.schemas import Token
from src.auth import service 
from src.auth.jwt import create_access_token

from src.barbers.schemas import Barber

from src.appointments.models import Appointment
from src.appointments import service as appointment_service

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    barber = service.authenticate_barber(db=db, username=form_data.username, password=form_data.password)
    if not barber:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth_config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": barber.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type":"bearer"}


@router.get("/me", response_model=Barber)
async def get_barbers_me(
    current_barber: Annotated[Barber, Depends(service.get_current_barber)]
):
    return current_barber

@router.get("/me/appointments")
async def get_own_appointments(
    current_barber: Annotated[Barber, Depends(service.get_current_barber)],
    db: Session = Depends(get_db)
):
    appointments = appointment_service.get_by_username(db=db, username=current_barber.username)
    return appointments

@router.get("/me/appointments/{appointment_date}")
async def get_own_appointments_on_date(
    appointment_date: str,
    current_barber: Annotated[Barber, Depends(service.get_current_barber)],
    db: Session = Depends(get_db)
):
    print("x")
    appointments = appointment_service.get_by_username_on_date(db=db, username=current_barber.username, appointment_date=appointment_date)
    return appointments