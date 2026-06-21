from datetime import date
from src.domain.descriptors.montant_positif import MontantPositif
from src.domain.entities.facture import Facture
from src.domain.mixins.serializable_mixin import SerializableMixin
from src.domain.mixins.auditable_mixin import AuditableMixin

class Paiement(SerializableMixin, AuditableMixin):
    montant = MontantPositif()

    def __init__(self, facture: Facture, montant: float, date_paiement: date = None):
        self.facture = facture
        self.montant = montant
        self.date_paiement = date_paiement or date.today()
        self._init_audit()

    def __call__(self):
        """
        Dunder __call__ : permet de faire paiement() comme si l'objet était une fonction.
        Ici, on l'utilise pour "exécuter" le paiement : il marque la facture comme payée.
        """
        if self.montant < self.facture.montant:
            raise ValueError(
                f"Paiement insuffisant: {self.montant} pour une facture de {self.facture.montant}€"
            )
        self.facture.marquer_payee()
        return f"Facture {self.facture.numero} payée ({self.montant})"

    def __repr__(self):
        return f"Paiement(facture={self.facture.numero!r}, montant={self.montant}€, date={self.date_paiement})"