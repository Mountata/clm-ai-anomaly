# tests/test_mixins.py
import time
from src.domain.entities.contrat import Contrat


def test_to_dict_contient_les_bons_champs(contrat):
    d = contrat.to_dict()
    assert d["reference"] == "CTR-001"
    assert d["montant"] == 15000


def test_to_dict_serialise_les_dates_en_string(contrat):
    d = contrat.to_dict()
    assert isinstance(d["date_fin"], str)  # pas un objet date, une string ISO


def test_to_dict_serialise_objet_imbrique(contrat):
    d = contrat.to_dict()
    assert isinstance(d["client"], dict)  # Client converti en dict, pas en objet brut
    assert d["client"]["nom"] == "Acme Corp"


def test_auditable_mixin_a_une_date_de_creation(contrat):
    assert contrat.cree_le is not None
    assert contrat.modifie_le is not None


def test_auditable_mixin_marquer_modifie_change_la_date(facture):
    date_initiale = facture.modifie_le
    time.sleep(0.01)
    facture.marquer_payee()  # appelle marquer_modifie() en interne
    assert facture.modifie_le > date_initiale