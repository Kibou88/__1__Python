# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-07-13
# Date de dernière modification: 2024-07-15
# ----------------------------------------------------------------
# version: 3.0
# - Ajout de message pour stocker le message à afficher (V2)
# - La valeur nombre est arrondi à 2 chiffres (V2)
# - Mise en forme du message à afficher (V2)
# - Suppression du round (V3)
# - Remplacement message de type 'str' par un type 'list' (V3)
# - Ajout de '+0.01' dans l'équation pour faire l'arrondit (V3)
# - Changement des variables: "nombre" -> "argent" (programme) (V3)
#                             "nombre" -> "monnaies" (fonction) (V3)
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import DEVISE_MEXICAINE


def decomposition_monnaie(monnaies: int) -> str:
    """
    Décompose le nombre en différents billets
    :param
    nombre (int): Argent à décomposer
    :return:
    liste_devise (list): stocke le message à afficher
    """
    liste_devise = []
    for key, value in DEVISE_MEXICAINE.items():
        if monnaies >= key:
            liste_devise.append(f"{value} : {int(round(monnaies,2) / key)}")
            monnaies = monnaies % key + 0.01

    return liste_devise

if __name__ == '__main__':
    try:
        argent = float(input("Entrez une quantité d'argent > "))
    except ValueError:
        print("Erreur de type. Inscrire un nombre!!")
    else:
        print("\n".join(decomposition_monnaie(argent)))

