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



import json

print(json.dumps(contrat.to_dict(), indent=2, default=str))

import time

f3 = Facture("FAC-003", contrat, 2000, date.today() + timedelta(days=10))
print(f3.to_dict())          # grâce à SerializableMixin
print(f3.cree_le)            # grâce à AuditableMixin

time.sleep(1)
f3.marquer_payee()
print(f3.modifie_le)         # différent de cree_le maintenant


c1 = Contrat("CTR-A", c, 10000, date.today() + timedelta(days=60), vecteur_embedding=[1, 0, 1])
c2 = Contrat("CTR-B", c, 8000, date.today() + timedelta(days=60), vecteur_embedding=[1, 0, 0.9])
c3 = Contrat("CTR-C", c, 5000, date.today() + timedelta(days=60), vecteur_embedding=[0, 1, 0])

print(c1 @ c2)   # proche de 1 → contrats similaires
print(c1 @ c3)   # proche de 0 → contrats différents