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
# - Changement de "int" dans la fonction par "float" (V4)
# - Remplacement '+0.01' par un round (V4)
# - Simplification de la formule pour afficher le nombre de billets/pièces (V4)
# - Ajout du join dans la fonction plutôt que dans le print (V4)
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import DEVISE_MEXICAINE


def decomposition_monnaie(monnaies: float) -> str:
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
            liste_devise.append(f"{value} : {int(monnaies // key)}")
            monnaies = round(monnaies % key, 2)

    return "\n".join(liste_devise)

if __name__ == '__main__':
    try:
        argent = float(input("Entrez une quantité d'argent > "))
    except ValueError:
        print("Erreur de type. Inscrire un nombre!!")
    else:
        print(decomposition_monnaie(argent))

