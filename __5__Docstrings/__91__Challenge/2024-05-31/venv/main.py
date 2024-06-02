# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-06-01
# Date de dernière modification: 2024-06-01
# ------------------------------------------
# version: 1.0
#-------------------------------------------

# Appelle des modules externes

# Appelle des modules internes
from constantes import LISTE_ELEVES
from moyenne import moyenne_eleves
from classement import classement_eleves

if __name__ == '__main__':

    dict_eleves = moyenne_eleves(LISTE_ELEVES)
    sorted_dict_eleves = classement_eleves(dict_eleves)
    for index_numb,infos_eleves in enumerate(sorted_dict_eleves): #Afficher le classement des élèves
        print(f"{index_numb+1}: {infos_eleves[0]} avec une moyenne de {infos_eleves[1]}/20")