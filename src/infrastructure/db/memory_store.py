# src/infrastructure/db/memory_store.py
from datetime import date, timedelta
from src.domain.entities.client import Client
from src.domain.entities.contrat import Contrat

# Stockage temporaire en mémoire (sera remplacé par PostgreSQL plus tard)
_contrats: list[Contrat] = []



def _seed_donnees_demo():
    """Crée quelques contrats de démo au démarrage, pour avoir des données à afficher."""
    client1 = Client("Acme Corp", "contact@acme.com", "12345678900012")
    client2 = Client("Globex SA", "contact@globex.com", "98765432100099")

    _contrats.append(
        Contrat("CTR-001", client1, 15000, date.today() + timedelta(days=90))
    )
    _contrats.append(
        Contrat("CTR-002", client2, 8000, date.today() + timedelta(days=30))
    )


def get_all_contrats() -> list[Contrat]:
    return _contrats


def add_contrat(contrat: Contrat) -> Contrat:
    _contrats.append(contrat)
    return contrat


def get_contrat_by_reference(reference: str) -> Contrat | None:
    for c in _contrats:
        if c.reference == reference:
            return c
    return None


_seed_donnees_demo()  # exécuté une fois à l'import du module