from app.schemas.email_models import EmailInput, AgentDecision


def classify_email(email: EmailInput) -> AgentDecision:
    text = f"{email.subject} {email.body}".lower()

    if "factura" in text or "invoice" in text or "pago" in text:
        return AgentDecision(
            category="factura",
            urgency="alta",
            suggested_action="seguimiento",
            confidence=0.88,
            reason="Detecté términos asociados a facturación o pago.",
            draft_reply=None,
        )

    if "reunión" in text or "meeting" in text or "agenda" in text:
        return AgentDecision(
            category="cliente",
            urgency="media",
            suggested_action="borrador",
            confidence=0.84,
            reason="El correo parece requerir coordinación o respuesta.",
            draft_reply="Hola, gracias por tu correo. Te propongo revisar horarios disponibles y te respondo en breve.",
        )

    if "newsletter" in text or "unsubscribe" in text:
        return AgentDecision(
            category="spam",
            urgency="baja",
            suggested_action="archivar",
            confidence=0.91,
            reason="Parece un correo promocional o newsletter.",
            draft_reply=None,
        )

    return AgentDecision(
        category="otro",
        urgency="baja",
        suggested_action="etiquetar",
        confidence=0.65,
        reason="No encontré señales claras; conviene revisar o etiquetar.",
        draft_reply=None,
    )