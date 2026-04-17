from pydantic import BaseModel
from typing import Literal, Optional


Category = Literal["cliente", "interno", "factura", "spam", "otro"]
Urgency = Literal["alta", "media", "baja"]
SuggestedAction = Literal["borrador", "etiquetar", "archivar", "seguimiento", "escalar"]


class EmailInput(BaseModel):
    sender: str
    subject: str
    body: str


class AgentDecision(BaseModel):
    category: Category
    urgency: Urgency
    suggested_action: SuggestedAction
    confidence: float
    reason: str
    draft_reply: Optional[str] = None