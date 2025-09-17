from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class WeatherResponse(BaseModel):
    temperature_c: float
    rainfall_mm: float
    alert: str


@router.get("/current", response_model=WeatherResponse)
async def current_weather(location: str) -> WeatherResponse:
    return WeatherResponse(temperature_c=30.0, rainfall_mm=2.0, alert="No alert")

