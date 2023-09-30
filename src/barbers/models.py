from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    surname = Column(String)

    created_at = Column(DateTime)

    appointments = relationship("Appointment", back_populates="owner")
