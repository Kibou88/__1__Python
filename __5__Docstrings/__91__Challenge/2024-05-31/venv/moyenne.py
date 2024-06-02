# moyenne.py
# But:
# Contient la fonction moyenne_eleves
#   => Renvoyer la valeur moyenne de chaque élève sous forme de dico
# -----------------------------------
# Date de création: 2024-06-01
# Date de dernière modification: 2024-06-01
# ------------------------------------------
# version: 1.0
#-------------------------------------------

def moyenne_eleves(LISTE_ELEVES):
    dict_eleves={}
    for eleves in LISTE_ELEVES:
        moyenne_float = sum(eleves[1])/len(eleves[1])
        moyenne = int(round(moyenne_float, 0)) # Retourne la moyenne arrondi à l'entier le + proche
        dict_eleves[eleves[0]] = moyenne # Sauvegarde de la moyenne avec l'élève associé
    return dict_eleves



if __name__ == '__main__':
    from constantes import LISTE_ELEVES

    print(moyenne_eleves(LISTE_ELEVES))