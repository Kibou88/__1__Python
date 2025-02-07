# 1 instance unique d'une classe
# - Créer une instance d'une classe et bloqué les autres
#---------------------------------------------------------

class MaVoiture():
    _instance = None

    def __init__(self):
        if MaVoiture._instance is not None:
            raise Exception("Une instance a déjà été créée")
        self.color = "rouge"
        self.marque = "ferrari"

    def __str__(self):
        return f'Voiture de marque {self.marque} et de couleur {self.color}'

    @staticmethod
    def getInstance():
        if MaVoiture._instance == None:
            MaVoiture._instance = MaVoiture()
        return MaVoiture._instance

voiture01 = MaVoiture.getInstance()
print(voiture01)

voiture02 = MaVoiture.getInstance()
print(voiture02)

voiture01.color = 'Jaune'
print(voiture01)
print(voiture02)
