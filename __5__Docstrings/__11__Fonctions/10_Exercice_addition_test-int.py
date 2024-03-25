# Exercice addition avec test si valeurs sont des nombres
# - Créer une fonction add qui teste si ces 2 paramètres sont des nombres
# sinon la fonction lève un ValueError
#############################################################################
def add(a: int = 0, b: int = 0) -> int:
    if isinstance(a, int) and isinstance(b, int):
    #si a et b sont des nombres int
        return a + b
    else:
        raise ValueError(f"Veuillez rentrer un nombre")


print(add(a=10, b=10))
#--------------------------------------------------------
def add(a: int, b: int) -> int:
    #Il faut que a et b soient des int
    # '-> int' précise que la fonction renvoie un int (indicatif ne change rien au résultat de la fonction)
    erreur = "Erreur : La fonction accepte uniquement des nombres"
    if not type(a) == int or not type(b) == int:
        raise ValueError(erreur)
    return a + b

print(add(5,6))