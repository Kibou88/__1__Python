# Fonction search
# - Apprendre à utiliser la fonction search
#---------------------------------------------
import re

"""
Va chercher dans l'entiéreté de la chaine
"""

a = re.search(r'\+', 'Pierre Dupont + Marie Dupont')
print(a)
b = re.match(r'ont', 'Pierre Dupont + Marie Dupont')
print(b)

# Même fonction que pour match
