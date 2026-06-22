# tests/test_descriptors.py
import pytest
from datetime import date, timedelta
from src.domain.descriptors.montant_positif import MontantPositif
from src.domain.descriptors.date_future import DateFuture


class Factice:
    montant = MontantPositif()
    date_fin = DateFuture()


def test_montant_positif_accepte_valeur_valide():
    obj = Factice()
    obj.montant = 100
    assert obj.montant == 100


def test_montant_positif_rejette_negatif():
    obj = Factice()
    with pytest.raises(ValueError):
        obj.montant = -50


def test_montant_positif_rejette_type_invalide():
    obj = Factice()
    with pytest.raises(TypeError):
        obj.montant = "cent euros"


def test_date_future_accepte_date_future():
    obj = Factice()
    obj.date_fin = date.today() + timedelta(days=10)
    assert obj.date_fin == date.today() + timedelta(days=10)


def test_date_future_rejette_date_passee():
    obj = Factice()
    with pytest.raises(ValueError):
        obj.date_fin = date.today() - timedelta(days=1)