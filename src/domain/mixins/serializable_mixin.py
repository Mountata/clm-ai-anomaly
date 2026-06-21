from datetime import date, datetime
from enum import Enum

class SerializableMixin:

    """ ajpute la capaciéde se trnsformer en dict  puis en json 
        Toute classe qui herite de ce mixin  recupere to_dict() facilement 

    """

    def to_dict(self) -> dict:

        resultat = {}
        for cle, valeur in self.__dict__.items():
            cle_public = cle[1:] if cle.startswith("_") else cle  # _montant -> "montant"

            resultat[cle_public] = self._serialiser_valeur(valeur)

        return resultat
    
    def _serialiser_valeur(self, valeur):
        # on gere les cas particulier qui ne sont pas du json natif

        if isinstance(valeur, (date, datetime)):
            return valeur.isoformat()
        
        if isinstance(valeur, Enum):
            return valeur.value
        if isinstance(valeur, SerializableMixin):
            return valeur.to_dict() # objet imbriquer (ex Facture.contrat)
        return valeur 




    

