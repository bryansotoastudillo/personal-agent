from fastapi import APIRouter
from app.schemas.email_models import EmailInput
from app.services.classifier import classify_email

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/classify")
def classify(email: EmailInput):
    decision = classify_email(email)
    return decision