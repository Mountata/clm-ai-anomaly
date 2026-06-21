# tests/test_entities.py
import pytest
from datetime import date, timedelta
from src.domain.entities.paiement import Paiement
from src.domain.entities.tache import Tache, PrioriteTache


# --- Tests sur Contrat ---

def test_contrat_duree_restante_jours(contrat):
    assert contrat.duree_restante_jours == 90


def test_contrat_non_expire(contrat):
    assert contrat.est_expire is False


def test_contrat_montant_negatif_leve_erreur(contrat):
    with pytest.raises(ValueError):
        contrat.montant = -1000


# --- Tests sur Facture ---

def test_facture_statut_en_attente(facture):
    assert facture.statut == "En attente"


def test_facture_marquer_payee_change_statut(facture):
    facture.marquer_payee()
    assert facture.statut == "Payée"


def test_facture_addition_deux_factures(facture, contrat):
    f2 = facture.__class__(
        numero="FAC-002",
        contrat=contrat,
        montant=3000,
        date_echeance=date.today() + timedelta(days=20)
    )
    total = facture + f2
    assert total == 8000  # 5000 + 3000


def test_facture_client_accessible_via_contrat(facture, client):
    assert facture.client == client


# --- Tests sur Paiement ---

def test_paiement_suffisant_marque_facture_payee(facture):
    paiement = Paiement(facture, montant=5000)
    paiement()
    assert facture.statut == "Payée"


def test_paiement_insuffisant_leve_erreur(facture):
    paiement = Paiement(facture, montant=1000)
    with pytest.raises(ValueError):
        paiement()


# --- Tests sur Tache ---

def test_tache_creation_non_terminee():
    t = Tache("Relancer le client", PrioriteTache.HAUTE)
    assert t.terminee is False


def test_tache_terminer():
    t = Tache("Relancer le client", PrioriteTache.HAUTE)
    t.terminer()
    assert t.terminee is True