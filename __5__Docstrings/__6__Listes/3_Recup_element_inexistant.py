# Récupérer un élément inexistant d'une liste
#-----------------------------------------------

liste = range(10)

index = 10

# print(liste[index]) # Retourne un IndexError

try:
    r = liste[index]
    print(r)
except IndexError:
    print(f"L'index {index} n'existe pas")

r = liste[index] if len(liste) > index else None
print(r)