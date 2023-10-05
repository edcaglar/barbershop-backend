from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, DateTime, func
from sqlalchemy.orm import relationship

from src.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_surname = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now(),)

    barber_id = Column(Integer, ForeignKey("barbers.id"), nullable=False)
    owner = relationship("Barber", back_populates="appointments")
