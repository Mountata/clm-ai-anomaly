from datetime import date
from src.domain.descriptors.montant_positif import MontantPositif
from src.domain.descriptors.date_future import DateFuture
from src.domain.entities.contrat import Contrat
from src.domain.mixins.serializable_mixin import SerializableMixin
from src.domain.mixins.auditable_mixin import AuditableMixin


class Facture(SerializableMixin, AuditableMixin):
    montant = MontantPositif()
    date_echeance = DateFuture()

    def __init__(self, numero: str, contrat: Contrat, montant: float, date_echeance: date):
        self.numero = numero
        self.contrat = contrat
        self.montant = montant
        self.date_echeance = date_echeance
        self.payee = False
        self._init_audit()

    @property
    def client(self):
        # Pratique : accéder au client directement depuis la facture,
        # sans dupliquer l'info (elle vient déjà de self.contrat)
        return self.contrat.client

    @property
    def statut(self) -> str:
        if self.payee:
            return "Payée"
        if self.date_echeance < date.today():
            return "En retard"
        return "En attente"

    def marquer_payee(self):

        self.payee = True
        self.marquer_modifie()

    def __add__(self, autre: "Facture") -> float:
        """
        Permet de faire: facture1 + facture2  → retourne le montant total.
        Dunder = méthode magique appelée automatiquement par l'opérateur +.
        """
        if not isinstance(autre, Facture):
            raise TypeError("On ne peut additionner que deux Factures entre elles")
        return self.montant + autre.montant

    def __repr__(self):
        return f"Facture(n°={self.numero!r}, montant={self.montant}€, statut={self.statut!r})"