# src/api/schemas/contrat_schema.py
from pydantic import BaseModel, Field
from datetime import date


class ContratCreate(BaseModel):
    """Schéma de validation pour la création d'un contrat."""
    reference: str = Field(..., example="CTR-003")
    client_nom: str = Field(..., example="Acme Corp")
    client_email: str = Field(..., example="contact@acme.com")
    client_siret: str = Field(..., example="12345678900012")
    montant: float = Field(..., gt=0, example=15000)  # gt=0 → doit être > 0
    date_fin: date = Field(..., example="2026-12-31")


class ContratResponse(BaseModel):
    """Schéma de la réponse retournée au client."""
    reference: str
    montant: float
    statut: str
    duree_restante_jours: int
    client: dict

    class Config:
        from_attributes = True