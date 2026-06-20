from datetime import date
from enum import Enum


class PrioriteTache(Enum):
    BASSE = "basse"
    MOYENNE = "moyenne"
    HAUTE = "haute"


class Tache:
    def __init__(self, titre: str, priorite: PrioriteTache = PrioriteTache.MOYENNE, date_limite: date = None):
        self.titre = titre
        self.priorite = priorite
        self.date_limite = date_limite
        self.terminee = False

    def terminer(self):
        self.terminee = True

    def __repr__(self):
        statut = "✓" if self.terminee else "✗"
        return f"Tache({statut} {self.titre!r}, priorité={self.priorite.value})"