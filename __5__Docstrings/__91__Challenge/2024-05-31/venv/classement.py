# classement.py
# But:
# Contient la fonction classement_eleves
#   => Renvoyer le classement des élèves par rapport à leur moyenne sous forme de dico
# -----------------------------------
# Date de création: 2024-06-01
# Date de dernière modification: 2024-06-01
# ------------------------------------------
# version: 1.0
#-------------------------------------------

def classement_eleves(dict_eleves):
    return sorted(dict_eleves.items(), key=lambda x:x[1], reverse=True) #Trie par ordre décroissant



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
