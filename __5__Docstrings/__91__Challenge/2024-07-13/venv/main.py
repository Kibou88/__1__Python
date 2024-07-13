# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-07-13
# Date de dernière modification: 2024-07-13
# ----------------------------------------------------------------
# version: 1.0
# -
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import DEVISE_MEXICAINE


def decomposition_monnaie(nombre: int):
    """
    Décompose le nombre en différents billets
    :param
    nombre (int): Argent à décomposer
    :return:
    affiche le billet et la quantité
    """
    for key, value in DEVISE_MEXICAINE.items():
        if nombre >= key:
            print(f"{value} : ", int(nombre / key))
            nombre -= key * int(nombre / key)

if __name__ == '__main__':
    try:
        nombre = float(input("Entrez une quantité d'argent > "))
    except ValueError:
        print("Erreur de type. Inscrire un nombre!!")
    else:
        decomposition_monnaie(nombre)