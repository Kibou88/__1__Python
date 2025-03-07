# Eviter le retour d'une erreur lorsque la clé est inexistante
#####################################################################
dic = {
    'Pierre': 'Serveur',
    'Julien': 'Libraire',
    'Marie': 'Ingenieure'
    }

prenom = 'Jacques'
prenom2 = 'Marie'

# Mauvaise façon de faire
# Retourne un 'KeyError'
# profession = dic[prenom]

# Retour un 'None' si la clé est absente
profession = dic.get(prenom)
profession2 = dic.get(prenom2)
print(profession)

print(f'La clé {prenom} est {profession if dic.get(prenom) != None else "absente"}')
print(f'La clé {prenom2} est {profession2 if dic.get(prenom2) != None else "absente"}')