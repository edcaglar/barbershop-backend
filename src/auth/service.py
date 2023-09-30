from sqlalchemy.orm import Session

from src.auth.schemas import AuthBarber
from src.auth.security import hash_password, check_password


def create_barber(db: Session, barber: AuthBarber):
    hashed_password = hash_password(barber.password)
    barber.password = hashed_password

    new_barber = AuthBarber(barber.model_dump())
    db.add(new_barber)
    db.commit()
    db.refresh(new_barber)
    return new_barber


