from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel


router = APIRouter()


class PestDetection(BaseModel):
    probable_pest: str
    confidence: float
    advice: str


@router.post("/detect", response_model=PestDetection)
async def detect_pest(image: UploadFile = File(...)) -> PestDetection:
    return PestDetection(
        probable_pest="Aphids",
        confidence=0.65,
        advice="Use neem-based biopesticide and monitor for spread.",
    )

