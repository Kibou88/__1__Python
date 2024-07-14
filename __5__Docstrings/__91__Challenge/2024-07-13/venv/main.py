# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-07-13
# Date de dernière modification: 2024-07-14
# ----------------------------------------------------------------
# version: 2.0
# - Ajout de message pour stocker le message à afficher (V2)
# - La valeur nombre est arrondi à 2 chiffres (V2)
# - Mise en forme du message à afficher (V2)
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import DEVISE_MEXICAINE


def decomposition_monnaie(nombre: int) -> str:
    """
    Décompose le nombre en différents billets
    :param
    nombre (int): Argent à décomposer
    :return:
    message (str): affiche le billet et la quantité
    """
    message = ""
    for key, value in DEVISE_MEXICAINE.items():
        if round(nombre,2) >= key:
            message += f"{value} : {int(round(nombre,2) / key)}//"
            nombre -= key * int(nombre / key)
    return message

if __name__ == '__main__':
    try:
        nombre = float(input("Entrez une quantité d'argent > "))
    except ValueError:
        print("Erreur de type. Inscrire un nombre!!")
    else:
        print(decomposition_monnaie(nombre).replace("//","\n"))

