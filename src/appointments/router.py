from fastapi import APIRouter, Path, Query
from typing import Annotated
from .schemas import Appointment

router = APIRouter(prefix="/appointments",)


@router.post("/")
def create_appointment(appointment: Appointment):
    return appointment
