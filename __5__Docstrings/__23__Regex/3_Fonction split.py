# Fonction split
# - Apprendre à utiliser la fonction split
#---------------------------------------------
import re

"""
Fonctionne comme la fonction split classique, sauf qu'on peut mettre plusieurs éléments à splitter
"""

texte = 'item01 | item02 - item03 - item04 | item05'

a = re.split(r' \| | - ', texte)
# \|: Permet de rechercher l'un ou l'autre des éléments après. Ici, soit '|', soit '-'
print(type(a))