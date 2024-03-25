# Exercice moyenne élèves
# - But: Calculer la moyenne des élèves et la sortir en dictionnaire
####################################################################
classe = {'Adrienne': [4, 18],
          'Joséphine': [10, 12, 20],
          'Margaret': [11],
          'Michel': [1],
          'Olivier': [1, 2, 3, 10, 7],
          'René': [17, 17, 20],
          'Édouard': [5, 17, 14, 12, 16]}


def moyenne_eleves(dict_):
    return {keys: sum(values) / len(values) for keys, values in classe.items()}

print(moyenne_eleves(classe))