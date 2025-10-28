from typing import List

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class MarketPrice(BaseModel):
    commodity: str
    price_per_quintal: float
    mandi: str
    state: str


@router.get("/prices", response_model=List[MarketPrice])
async def get_prices(state: str, commodity: str) -> List[MarketPrice]:
    return [
        MarketPrice(
            commodity=commodity, price_per_quintal=2200.0, mandi="Nashik", state=state
        ),
        MarketPrice(
            commodity=commodity, price_per_quintal=2100.0, mandi="Pune", state=state
        ),
    ]

