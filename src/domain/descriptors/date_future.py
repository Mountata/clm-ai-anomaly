from datetime import date, timedelta,datetime


class DateFuture:
    """
    Descripteur qui garantit qu'une date est aujourd'hui ou dans le futur.
    """

    def __set_name__(self, owner, name):
        self.nom_prive = f"_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.nom_prive, None)

    def __set__(self, instance, value):
        if isinstance(value, datetime):
            value = value.date()  # on normalise: on travaille toujours avec une date, pas un datetime

        if not isinstance(value, date):
            raise TypeError(f"La date doit être un objet date, reçu: {type(value).__name__}")

        if value < date.today():
            raise ValueError(f"La date doit être aujourd'hui ou dans le futur, reçu: {value}")

        setattr(instance, self.nom_prive, value)

# ---------- TESTS (pour vérifier que ça fonctionne) ----------
if __name__ == "__main__":
    class Contrat:
        date_debut = DateFuture()
        date_fin = DateFuture()

    t = Contrat()

    # Test 1 : Aujourd'hui (OK)
    t.date_debut = date.today()
    print(f"✅ date_debut acceptée : {t.date_debut}")

    # Test 2 : Dans le futur (+30 jours) (OK)
    t.date_fin = date.today() + timedelta(days=30)
    print(f"✅ date_fin acceptée : {t.date_fin}")

    # Test 3 : Dans le passé (ERREUR)
    try:
        t.date_debut = date(2020, 1, 1)
    except ValueError as e:
        print(f"❌ Erreur attrapée (passé) : {e}")

    # Test 4 : On essaie de mettre un texte (ERREUR)
    try:
        t.date_debut = "2025-01-01"
    except TypeError as e:
        print(f"❌ Erreur attrapée (type) : {e}")