from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from src.database import Base


class Barber(Base):
    __tablename__ = "barbers"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False, server_default=text('now()'))

    appointments = relationship("Appointment", back_populates="owner")
