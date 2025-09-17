from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class AdvisoryRequest(BaseModel):
    location: str
    crop: Optional[str] = None
    soil_type: Optional[str] = None
    language: Optional[str] = "en"


class Recommendation(BaseModel):
    title: str
    description: str


class AdvisoryResponse(BaseModel):
    recommendations: List[Recommendation]


@router.post("/", response_model=AdvisoryResponse)
async def get_advisory(payload: AdvisoryRequest) -> AdvisoryResponse:
    recommendations = [
        Recommendation(
            title="Irrigation",
            description="Irrigate based on soil moisture and upcoming rainfall forecast.",
        ),
        Recommendation(
            title="Fertilizer",
            description="Apply NPK as per soil test recommendations to avoid overuse.",
        ),
    ]
    return AdvisoryResponse(recommendations=recommendations)

