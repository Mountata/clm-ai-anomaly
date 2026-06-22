from datetime import datetime
class AuditableMixin:
    """
    Ajoute le suivi automatique : date de creation et date de derniere modification
        AuditableMixin
    """
    def _init_audit(self):
        # on appelle ca explicitement dans __init__de la classe enfant 
        # un mixin n'a pas de __init__ propre , donc pas d'auto -iit magique 

        self.cree_le = datetime.now()
        self.modifie_le = datetime.now()

    def marquer_modifie(self):
        self.modifie_le = datetime.now()   