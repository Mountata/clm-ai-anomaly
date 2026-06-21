from datetime import date
from src.domain.descriptors.montant_positif import MontantPositif
from src.domain.descriptors.date_future import DateFuture
from src.domain.entities.client import Client
from src.domain.mixins.serializable_mixin import SerializableMixin
from src.domain.mixins.auditable_mixin import AuditableMixin
import math

class Contrat(SerializableMixin, AuditableMixin):
    montant = MontantPositif()    # utilise le descripteur qu'on a déjà testé
    date_fin = DateFuture()       # idem

    def __init__(self, reference: str, client: Client, montant: float, date_fin: date, vecteur_embedding: list = None):
        self.reference = reference
        self.client = client
        self.montant = montant        # passe par le descripteur MontantPositif → validation auto
        self.date_fin = date_fin      # passe par le descripteur DateFuture → validation auto
        self.statut = "actif"
        self.vecteur_embedding = vecteur_embedding or []  # simulé pour l'instant, vide par défaut
        
        self._init_audit()


    def __matmul__(self, autre: "Contrat") -> float:
        """
        Dunder __matmul__ : appelé automatiquement par l'opérateur @.
        Simule un score de similarité cosinus entre deux contrats,
        en se basant sur leurs vecteurs d'embedding.
        Plus tard (Phase 3), ces vecteurs viendront d'un vrai modèle IA.
        """
        if not isinstance(autre, Contrat):
            raise TypeError("__matmul__ attend un autre Contrat")
        if not self.vecteur_embedding or not autre.vecteur_embedding:
            raise ValueError("Les deux contrats doivent avoir un vecteur_embedding non vide")
        if len(self.vecteur_embedding) != len(autre.vecteur_embedding):
            raise ValueError("Les vecteurs doivent avoir la même dimension")

        # Produit scalaire (dot product) — le coeur du calcul de similarité
        produit_scalaire = sum(a * b for a, b in zip(self.vecteur_embedding, autre.vecteur_embedding))

        # Normalisation (norme de chaque vecteur)
        norme_self = math.sqrt(sum(a ** 2 for a in self.vecteur_embedding))
        norme_autre = math.sqrt(sum(a ** 2 for a in autre.vecteur_embedding))

        # Similarité cosinus = produit scalaire / (norme1 * norme2)
        return produit_scalaire / (norme_self * norme_autre)
    
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