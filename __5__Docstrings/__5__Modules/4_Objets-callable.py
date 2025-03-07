# Objets "callable"
# - Permet de comprendre ce que sont les objets "callables"
###########################################################
import pprint

print(callable(pprint)) # Renvoie un false car c'est un module et non la fonction

from pprint import pprint
print(callable(pprint)) # Renvoie True car la fonction est appelable

#/!\Si l'attribut n'est pas "callable", Python retourne:
#   TypeError: 'str' object is not callable
import os
print(os.name()) # name du module os n'est pas callable