from pydantic import BaseModel
from datetime import datetime


class AppointmentBase(BaseModel):
    customer_name: str
    customer_surname: str
    customer_phone: int
    barber_id: int
    date: datetime.date
    time: datetime.time


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
