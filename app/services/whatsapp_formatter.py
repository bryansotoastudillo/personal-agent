from app.schemas.email_models import EmailInput, AgentDecision


def format_whatsapp_message(email: EmailInput, decision: AgentDecision) -> str:
    lines = [
        f"Correo nuevo de: {email.sender}",
        f"Asunto: {email.subject}",
        "",
        "Resumen:",
        decision.reason,
        "",
        "Clasificación:",
        f"- categoría: {decision.category}",
        f"- urgencia: {decision.urgency}",
        f"- acción sugerida: {decision.suggested_action}",
        f"- confianza: {decision.confidence:.2f}",
    ]

    if decision.draft_reply:
        lines.extend([
            "",
            "Borrador sugerido:",
            decision.draft_reply,
        ])

    lines.extend([
        "",
        'Responde: "aprobar", "editar", "archivar", o escribe una instrucción',
    ])

    return "\n".join(lines)