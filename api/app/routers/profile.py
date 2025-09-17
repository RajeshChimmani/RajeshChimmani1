from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class FarmerProfile(BaseModel):
    name: str
    phone: Optional[str] = None
    language: str = "en"
    location: Optional[str] = None


@router.get("/me", response_model=FarmerProfile)
async def get_profile() -> FarmerProfile:
    return FarmerProfile(
        name="Demo Farmer", phone="9999999999", language="hi", location="Nashik"
    )

