class Client:
    def __init__(self, nom: str, email: str, siret: str):
        self.nom = nom
        self.email = email
        self.siret = siret

    def __repr__(self):
        return f"Client(nom={self.nom!r}, email={self.email!r})"