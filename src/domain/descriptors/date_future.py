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

