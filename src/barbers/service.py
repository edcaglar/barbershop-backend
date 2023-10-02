from sqlalchemy.orm import Session

from . import models, schemas
from src.auth.security import hash_password, check_password



def get_barber(db: Session, id: int):
    return db.query(models.Barber).filter(models.Barber.id == id).first()


def get_barbers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_barber_by_username(db: Session, username: str):
    return db.query(models.Barber).filter(models.Barber.username == username).first()
    
def create_barber(db: Session, barber: schemas.BarberCreate):
    hashed_password = hash_password(barber.password)
    barber.password = hashed_password
    new_barber = models.Barber(barber.model_dump())
    db.add(new_barber)
    db.commit()
    db.refresh(new_barber)
    return new_barber
