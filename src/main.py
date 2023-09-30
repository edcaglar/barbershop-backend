from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings

from src.barbers.router import router as barbers_router
from src.appointments.router import router as appointments_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(barbers_router, prefix="/barbers", tags=["Barbers"])
app.include_router(appointments_router,
                   prefix="/appointments", tags=["Appointments"])
