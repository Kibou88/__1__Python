# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-06-01
# Date de dernière modification: 2024-06-05
# ----------------------------------------------------------------
# version: 5.0
# - Added EOR (V2)
# - Compréhension liste pour l'affichage + fonction 'join' (V2)
# - Déplacement de l'affichage du classement dans le module 'classement' (V3)
# - Ajout de l'EOR + join dans la fonction 'classement_eleves' (V4)
# - Optimisation du code et conformité PEP8 (V5)
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import LISTE_ELEVES, EOR


def moyenne_eleves(LISTE_ELEVES):
    return {nom: int(round(sum(notes)/len(notes))) for nom, notes in LISTE_ELEVES}

def classement_eleves(dict_eleves):
    sorted_dict_eleves = sorted(dict_eleves.items(), key = lambda x:x[1], reverse=True) #Trie par ordre décroissant
    return EOR.join(
            f"{index_numb:2} : {nom_eleve} avec une moyenne de {moy_eleve}/20"
            for index_numb,(nom_eleve,moy_eleve) in enumerate(sorted_dict_eleves, 1)
            )



if __name__ == '__main__':
    dict_eleves = moyenne_eleves(LISTE_ELEVES)
    print(classement_eleves(dict_eleves))
