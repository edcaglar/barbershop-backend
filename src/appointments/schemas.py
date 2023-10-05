from pydantic import BaseModel

from datetime import datetime, date, time

class AppointmentBase(BaseModel):
    customer_name: str
    customer_surname: str
    customer_phone: int
    appointment_date: date
    appointment_time: str
    barber_id: int


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
