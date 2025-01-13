# Fonction match
# - Apprendre à utiliser la fonction match
#---------------------------------------------
import re

# Ajout du 'r'
print('\tBonjour') # \t va compter comme une tabulation
print(r'\tBonjour') # \t va compter comme des caractères

a = re.match(r'.+', 'Pierre Dupont')
# print(a) # Va retourner un match object
# print(a.group())

b = re.match(r'(\w+)\s(\w+)', 'Pierre Dupont 4') # Les () permettent de créer un groupe
print(b.group(0)) # Affiche l'entièreté du match
print(b.group(1)) # groupe 1
print(b.group(2)) # groupe 2
# print(b.groupdict())
# group(0) = group(1) + ..... + group(x)

# Nommer les groupes. Pas utile
c = re.match(r'(?P<prenom>\w+) (?P<nom>\w+)', 'Pierre Dupont 4')
print(c.group('prenom'))
print(c.group('nom'))

print(c.groups()) # Affiche le résultat des groupes sous forme de liste
print(c.groupdict()) # Affiche le résultat des groupes sous forme de dictionnaire
# /!\ N'hésite de nommer les groupes /!\