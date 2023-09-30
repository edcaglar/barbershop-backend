from fastapi import APIRouter, Path, Query, status
from fastapi import status, HTTPException
from typing import Annotated

from .schemas import BarberBase, BarberIn, BarberOut

router = APIRouter(prefix="/barbers",)

# Form fields in fastapi ? json yerine form kullaniliyormus
# arastir.


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_barber(barber: BarberIn) -> BarberOut:
    return barber


# Query le=10 deneme amacli yazildi
# Max 10 sayisina kadar girilebilmesi icin query validation
@router.get("/{id}")
def get_barber(barber_id: Annotated[int, Path(title="The ID of the barber to get", gt=0, le=10)]):

    # if not barber:
    # raise HTTPException(status_code=404, detail="Barber not found.")
    # return barber
    return barber_id
