from src.domain.mixins.serializable_mixin import SerializableMixin
from src.domain.mixins.auditable_mixin import AuditableMixin

class Client(SerializableMixin, AuditableMixin):
    def __init__(self, nom: str, email: str, siret: str):
        self.nom = nom
        self.email = email
        self.siret = siret
        self._init_audit()

    def __repr__(self):
        return f"Client(nom={self.nom!r}, email={self.email!r})"