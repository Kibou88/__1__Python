# Jeu de rôle version Docstring
###############################

import random

ENNEMY_HEALTH=50
PLAYER_HEALTH=50
NUMBER_OF_POTIONS=3
SKIP_TURN=False

while True:

    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN=False
    else:
        userChoice=""
        while userChoice not in ["1","2"]:
            userChoice=input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)? ")

            if userChoice=="1": #Attaque
                yourAttack=random.randint(5,10)
                ENNEMY_HEALTH-=yourAttack
                print(f"Vous avez infligé {yourAttack} points de dégâts à l'ennemi")
            elif userChoice=="2": #Potion
                usePotion=random.randint(15,50)
                print(f"La potion vous a redonné {usePotion} points de vie")
                SKIP_TURN=True

    if ENNEMY_HEALTH<=0:
        print("Tu as gagné!!")
        break

    #Attaque de l'ennemi
    ennemyAttack=random.randint(5,15)
    PLAYER_HEALTH-= ennemyAttack
    print(f"L'ennemi vous a infligé {ennemyAttack} HP")

    if PLAYER_HEALTH<=0:
        print("Tu as perdu")
        break

    #Stats
    print(f"Il vous reste {PLAYER_HEALTH} points de vie")
    print(f"Il reste {ENNEMY_HEALTH} points de vie à l'ennemi")
    print("-"*50)

print("Fin du jeu")