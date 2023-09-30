from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_surname = Column(String)
    customer_phone = Column(String)
    date = Column(Date)
    time = Column(Time)
    created_at = Column(DateTime)

    barber_id = Column(Integer, ForeignKey("barbers.id"))
    owner = relationship("Barber", back_populates="appointments")
