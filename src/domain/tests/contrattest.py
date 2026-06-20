from datetime import date, timedelta
from src.domain.entities.client import Client
from src.domain.entities.contrat import Contrat

c = Client("Acme Corp", "contact@acme.com", "12345678900012")
contrat = Contrat(
    reference="CTR-001",
    client=c,
    montant=15000,
    date_fin=date.today() + timedelta(days=90)
)

print(contrat)
print(contrat.duree_restante_jours)  # ~90
print(contrat.est_expire)            # False

# Test de validation héritée du descripteur :
contrat.montant = -100  # doit lever ValueError