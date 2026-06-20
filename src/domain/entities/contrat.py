from datetime import date
from src.domain.descriptors.montant_positif import MontantPositif
from src.domain.descriptors.date_future import DateFuture
from src.domain.entities.client import Client


class Contrat:
    montant = MontantPositif()    # utilise le descripteur qu'on a déjà testé
    date_fin = DateFuture()       # idem

    def __init__(self, reference: str, client: Client, montant: float, date_fin: date):
        self.reference = reference
        self.client = client
        self.montant = montant        # passe par le descripteur MontantPositif → validation auto
        self.date_fin = date_fin      # passe par le descripteur DateFuture → validation auto
        self.statut = "actif"

    @property
    def duree_restante_jours(self) -> int:
        """
        Calculée à la volée, jamais stockée : toujours à jour.
        C'est ça l'intérêt d'une @property face à un simple attribut.
        """
        return (self.date_fin - date.today()).days

    @property
    def est_expire(self) -> bool:
        return self.duree_restante_jours < 0

    def __repr__(self):
        return (
            f"Contrat(ref={self.reference!r}, client={self.client.nom!r}, "
            f"montant={self.montant}€, restant={self.duree_restante_jours}j)"
        )