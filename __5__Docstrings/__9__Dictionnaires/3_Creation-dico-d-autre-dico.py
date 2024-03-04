# Création d'un dico à partir d'un autre dico
# - Corrigé d'un exercice sur Docstring avec la fonction 'setdefault'
#####################################################################
names = {
            "Patrick": "Smith",
            "Julie": "Mercier",
            "Maxime": "Moulin",
            "Gérard": "Moulin",
            "Rose": "Mercier",
            "Clara": "Smith",
            "John": "Moulin",
            "Michel": "Smith",
        }

resultat = {}
for key, value in names.items():
    resultat.setdefault(value, []).append(key)
print(resultat)
""" EXPLICATIONS:   https://www.docstring.fr/formations/exercices/166/?module=12&session=6&course=1&back=6&tab=solution

>>> dict = {"Moulin": ["Jean"]}
>>> dict.setdefault("Moulin", [])
["Jean"]

Dans le code ci-dessus, on utilise setdefault sur la clé "Moulin". Comme cette clé existe déjà dans le dictionnaire dict,
la méthode setdefault nous retourne la liste associée à cette clé dans le dictionnaire (la liste ["Jean"]).

Dans le cas d'une clé qui n'existe pas, elle sera créée, avec la valeur que nous passon en 2e argument à la méthode 
setdefault :

>>> dict = {}
>>> dict.setdefault("Smith", [])
>>> print(dict)
{'Smith': []}

Cela nous permet, dans le cas de l'énoncé de cet exercice, d'utiliser directement la méthode append après la 
méthode setdefault.

    - Si la clé n'existe pas, on insère une liste vide. setdefaultretournera donc une liste vide, dans laquelle on peut 
         utiliser append pour insérer le prénom de la première personne.
    - Si la clé existe, cela signifie qu'on a déjà au moins un prénom associé à un nom de famille, et ce prénom est 
        nécessairement contenu dans une liste. Là encore, nous pouvons donc directement utiliser la méthode append pour 
        insérer les prénoms suivants dans le dictionnaire.
"""