from sqlalchemy.orm import Session

from . import models, schemas
from src.auth.security import hash_password



def get(db: Session, id: int):
    return db.query(models.Barber).filter(models.Barber.id == id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Barber).offset(skip).limit(limit).all()

def get_by_username(db: Session, username: str):
    return db.query(models.Barber).filter(models.Barber.username == username).first()
    
def create(db: Session, barber: schemas.BarberCreate):
    new_barber = models.Barber(**barber.model_dump(exclude=["password"]), hashed_password=hash_password(barber.password))
    db.add(new_barber)
    db.commit()
    db.refresh(new_barber)
    return new_barber
