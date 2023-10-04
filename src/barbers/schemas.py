from pydantic import BaseModel
from datetime import datetime

from src.appointments.schemas import Appointment


class BarberBase(BaseModel):
    name: str
    surname: str
    username: str


class BarberCreate(BarberBase):
    password: str


class BarberOut(BarberBase):
    pass


class Barber(BarberBase):
    id: int
    appointments: list[Appointment] = []
    created_at: datetime

    class Config:
        from_attributes = True
