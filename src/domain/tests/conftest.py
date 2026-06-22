# tests/conftest.py
import pytest
from datetime import date, timedelta
from src.domain.entities.client import Client
from src.domain.entities.contrat import Contrat
from src.domain.entities.facture import Facture


@pytest.fixture
def client():
    return Client("Acme Corp", "contact@acme.com", "12345678900012")


@pytest.fixture
def contrat(client):
    return Contrat(
        reference="CTR-001",
        client=client,
        montant=15000,
        date_fin=date.today() + timedelta(days=90)
    )


@pytest.fixture
def facture(contrat):
    return Facture(
        numero="FAC-001",
        contrat=contrat,
        montant=5000,
        date_echeance=date.today() + timedelta(days=15)
    )