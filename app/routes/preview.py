from fastapi import APIRouter
from app.schemas.email_models import EmailInput
from app.services.classifier import classify_email
from app.services.whatsapp_formatter import format_whatsapp_message

router = APIRouter(prefix="/preview", tags=["preview"])


@router.post("/whatsapp")
def preview_whatsapp(email: EmailInput):
    decision = classify_email(email)
    message = format_whatsapp_message(email, decision)

    return {
        "decision": decision,
        "whatsapp_message": message
    }