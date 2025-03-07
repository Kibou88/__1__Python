# Nombre mystère
# - Demander à l'utilisateur de deviner un nombre entre 1 et 100. Il a 10 coups
###############################################################################
import random

#Variables globales
TRY=10
NOMBRE_MYSTERE=random.randint(1,101)

nombreUser=0

while nombreUser!=NOMBRE_MYSTERE and TRY>0:
    print(f"Il vous reste {TRY} coups")
    nombreUser=input("Devinez le nombre: ")

    if nombreUser.isdigit():
        nombreUser = int(nombreUser)

        if nombreUser == NOMBRE_MYSTERE:  # L'utilisateur a trouver le nombre mystère
            print(f"Bien joué. Vous avez trouvé le nombre {NOMBRE_MYSTERE} en {TRY} coups\n")
            pass
        elif nombreUser < NOMBRE_MYSTERE:  # Le nombre utilisateur est inférieur à celui du nombre mystère
            print("Vous êtes en-dessous\n")
            TRY -= 1
        elif nombreUser > NOMBRE_MYSTERE:  # Le nombre utilisateur est supérieur à celui du nombre mystère
            print("Vous êtes au-dessus\n")
            TRY -= 1
        else:
            print("Ce cas n'est pas possible")

    else:
        print("Veuillez entrer un nombre valide\n")

if TRY==0:
    print("Perdu!! GAME OVER!!")