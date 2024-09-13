# main.py
# But:
# Contient la logique du code
# -----------------------------------
# Date de création: 2024-09-13
# Date de dernière modification: 2024-09-13
# ------------------------------------------
# version: 1.0
# -
#-------------------------------------------

# Appel des modules externes
import random


# Variables globales
NOMBRE_MYSTERE = random.randint(1,100)


class Game_Mystere():

    def __init__(self, nombre_essais, essais_restants):
        self.nombres_essais = nombre_essais
        self.essais_restants = essais_restants
        self.NOMBRE_MYSTERE = NOMBRE_MYSTERE

    def bigger(self):
        print(f"\nLe nombre mystère est plus grand\n")
        return self.essais_restants - 1

    def smaller(self):
        print(f"\nLe nombre mystère est plus petit\n")
        return self.essais_restants - 1

    def user_try(self):
        print(f"\nEssai possible: {essais_restants}/{nombre_essais}")
        return int(input("Veuillez entre un nombre entre 1 et 100: "))


if __name__ == "__main__":
    print("Bienvenue dans le jeu Le Nombre Mystère\n")
    nombre_essais = int(input("Veuillez choisir le nombre d'essai maximum: "))

    essais_restants = nombre_essais
    nombre_utilisateur = 0

    while essais_restants > 0 and nombre_utilisateur != NOMBRE_MYSTERE:
        jeu_mystere = Game_Mystere(nombre_essais, essais_restants)
        nombre_utilisateur = jeu_mystere.user_try()

        if NOMBRE_MYSTERE > nombre_utilisateur:
            essais_restants = jeu_mystere.bigger()
        elif NOMBRE_MYSTERE < nombre_utilisateur:
            essais_restants = jeu_mystere.smaller()

    print("Fin du jeu")
