# Gestion EAFP et LBYL
# - Apprendre à gérer les façons de programmer EAFP et LBYL
#################################################################
"""
LBYL: Look Before You Leap (Regarde avant de sauter)
EAFP: it's Easier to Ask for Forgiveness than Permission (Il est plus facile de demander pardon que de demander la permission)
"""
dict={"nom":"toto"}

# LBYL: On vérifie avant de faire une ligne de code

if "cle" in dict:
    print(dict["cle"])

# EAFP: Try-Except
try:
    print(dict["cle"])
except:
    pass

# Différences entre les 2:
liste=[1, 2, "test", 3]

# -> LBYL
for i in liste:
    if not str(i).isdigit():
        liste.remove(i)
total=sum(liste)
print("LBYL: ", total)

# -> EAFP
liste=[1, 2, "test", 3]
try:
    total=sum(liste)
except:
    total=0
print("EAFP: ", total)
