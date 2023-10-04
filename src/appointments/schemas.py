from pydantic import BaseModel
from datetime import datetime, date, time

class AppointmentBase(BaseModel):
    customer_name: str
    customer_surname: str
    customer_phone: int
    barber_id: int
    appointment_date: date
    appointment_time: time


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
