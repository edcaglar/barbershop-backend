from fastapi import APIRouter, Path, Query, Depends
from fastapi import status, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

from src.database import get_db
from . import schemas, service

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Barber)
def create_barber(barber: schemas.BarberCreate, db: Session = Depends(get_db)) -> schemas.Barber:
    db_barber = service.get_by_username(db=db, username=barber.username)
    if db_barber:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists.")
    
    return service.create(db=db, barber=barber)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.Barber])
def get_barbers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    barbers = service.get_all(db=db, skip=skip, limit=limit)
    return barbers


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Barber)
def get_barber(id: int, db: Session = Depends(get_db)) -> schemas.Barber:
    barber = service.get(db=db, id=id)
    if not barber:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Barber not exists.")
    
    return barber

