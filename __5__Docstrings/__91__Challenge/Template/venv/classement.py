# classement.py
# But:
# Contient la fonction classement_eleves
#   => Renvoyer le classement des élèves par rapport à leur moyenne sous forme de dico
# -----------------------------------
# Date de création: 2024-06-01
# Date de dernière modification: 2024-06-01
# -------------------------------------------------------------------
# version: 2.0
# - Essai mise en place générateur pour affichage du classement (V2)
# - Remplacement ternaire par formatage f-string (V2)
#--------------------------------------------------------------------

def classement_eleves(dict_eleves):
    sorted_dict_eleves=sorted(dict_eleves.items(), key=lambda x:x[1], reverse=True) #Trie par ordre décroissant
    affichages=(
            f"{index_numb:2} : {nom_eleve} avec une moyenne de {moy_eleve}/20"
            for index_numb,(nom_eleve,moy_eleve) in enumerate(sorted_dict_eleves, 1))

    for affichage in affichages:
        print(affichage)


if __name__ == '__main__':
    dict_eleves = {'Tao': 11,
                   'Josette': 13,
                   'Patrick': 9,
                   'Pema': 10,
                   'Jean': 6,
                   'Bixente': 12,
                   'Paco': 8,
                   'Chuluun': 15,
                   'Marie': 14,
                   'Mohamed': 16}
    classement_eleves(dict_eleves)
