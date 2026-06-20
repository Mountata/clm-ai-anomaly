from datetime import date, timedelta
from src.domain.entities.client import Client
from src.domain.entities.contrat import Contrat
from datetime import timedelta
from src.domain.entities.facture import Facture
from src.domain.entities.paiement import Paiement
from src.domain.entities.tache import Tache, PrioriteTache
c = Client("Acme Corp", "contact@acme.com", "12345678900012")
contrat = Contrat(
    reference="CTR-001",
    client=c,
    montant=15000,
    date_fin=date.today() + timedelta(days=90)
)

print(contrat)
print(contrat.duree_restante_jours)
print(contrat.est_expire)  


f1 = Facture("FAC-001", contrat, 5000, date.today() + timedelta(days=15))
f2 = Facture("FAC-002", contrat, 3000, date.today() + timedelta(days=30))

print(f1)
print(f1 + f2)          # → 8000 grâce à __add__
print(f1.statut)        # → "En attente"
f1.marquer_payee()
print(f1.statut)        # → "Payée"


p = Paiement(f1, 5000)
print(p())               # exécute le paiement
print(f1.statut)         # → "Payée"

t = Tache("Relancer le client Acme", PrioriteTache.HAUTE)
print(t)
t.terminer()
print(t)