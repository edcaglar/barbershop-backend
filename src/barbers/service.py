from sqlalchemy.orm import Session

from . import models, schemas


def get_barber(db: Session, barber_id: int):
    return db.query(models.Barber).filter(models.Barber.id == barber_id).first()


def get_barbers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_barber(db: Session, user: schemas.BarberCreate):
    
