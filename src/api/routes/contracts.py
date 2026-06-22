from fastapi import APIRouter, HTTPException
from src.infrastructure.db.memory_store import (
    get_all_contrats,
    add_contrat,
    get_contrat_by_reference
)
from src.api.schemas.contrat_schema import ContratCreate
from src.domain.entities.client import Client
from src.domain.entities.contrat import Contrat

router = APIRouter(prefix="/contrats", tags=["Contrats"])


@router.get("/")
def lister_contrats():
    contrats = get_all_contrats()
    return [c.to_dict() for c in contrats]


@router.get("/{reference}")
def get_contrat(reference: str):
    contrat = get_contrat_by_reference(reference)
    if contrat is None:
        raise HTTPException(status_code=404, detail=f"Contrat {reference} introuvable")
    return contrat.to_dict()


@router.post("/", status_code=201)
def creer_contrat(data: ContratCreate):
    # Vérifie que la référence n'existe pas déjà
    if get_contrat_by_reference(data.reference):
        raise HTTPException(
            status_code=409,
            detail=f"Un contrat avec la référence {data.reference} existe déjà"
        )

    # Crée les objets domaine à partir des données validées par Pydantic
    client = Client(data.client_nom, data.client_email, data.client_siret)
    contrat = Contrat(
        reference=data.reference,
        client=client,
        montant=data.montant,
        date_fin=data.date_fin
    )

    add_contrat(contrat)
    return contrat.to_dict()