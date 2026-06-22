class MontantPositif:

    def __set_name__(self, owner, name):
        # Appelé automatiquement par python quon on ecrit :
        # montant = MontantPositif
        # owner = classe (ex: Facture), name = "montant"

        self.nom_prive = f"_{name}"

    def __get__(self, instance, owner):
        # instance = objet une facture precise
        # owner la classe
        if instance is None:
            return self # acces via la classe pas l'instance 
        
        return getattr(instance, self.nom_prive, None)
    
    def __set__(self, instance, value):
        
        if not isinstance(value, (int, float)):
            raise TypeError(f"Le montant doit etre un nombre : {type(value).__name__}")
        if value <0 :
            raise ValueError(f"le montant doit etre positif ou nul:, recu:{value}")
        
        setattr(instance, self.nom_prive, value)
