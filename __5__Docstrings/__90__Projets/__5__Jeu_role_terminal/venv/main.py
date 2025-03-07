# Jeu de rôle via terminal
# - Permet de faire un duel avec un ennemi (PC)
# - Les 2 attaquants auront chacun 50HP
# - L'utilisateur aura 3 potions (à chaque utilisation, un tour est sauté). Chaque potion donne entre 15 et 50 HP
#       et fait des attaques entre 5 et 10 HP
# - L'ennemi n'as pas de potions, fait des attaques entre 5 et 15 HP
#-------------------------------------------------------------------------
import emojis
import random
# Déclaration variables globales
ENNEMY_HEALTH=50
USER_HEALTH=50
NUMBER_OF_POTIONS=3
SKIP_TURN=False

while ENNEMY_HEALTH>=0 and USER_HEALTH>=0: #Tant qu'un des 2 attaquants à des HP
    #Affiche des emojis dans le code

    if not SKIP_TURN: #Si le joueur a utilisé une potion, SKIP_TURN passe à True
        print(f"Il vous reste {USER_HEALTH} HP et l'ennemi {ENNEMY_HEALTH} HP")
        userChoice=input(emojis.encode("Souhaitez-vous attaquer :crossed_swords: (1) ou utiliser une potion :test_tube: (2) ? "))
    else:
        userChoice = "-33"  # Va permettre de tomber dans le cas où le joueur saute son tour


    userAttack=0
    ennemyAttack=0
    if userChoice.isdigit() and userChoice in ["1","2"] or userChoice=="-33": #Si le choix user est un nombre ET inférieur à 2
        match userChoice:
            case "1":
                userAttack=random.randint(5,10)
                ennemyAttack=random.randint(5,15)
                print(emojis.encode(f"Vous avez infligés {userAttack} HP :drop_of_blood: à l'ennemi"))
                print(emojis.encode(f"L'ennemi vous a infligé {ennemyAttack} HP :drop_of_blood:"))

            case "2":
                if NUMBER_OF_POTIONS>0:
                    userPotion=random.randint(15,50)
                    ennemyAttack=random.randint(5,15)
                    print(emojis.encode(f"Vous avez récupérés {userPotion} HP :mending_heart:"))
                    print(emojis.encode(f"L'ennemi vous a infligé {ennemyAttack} HP :drop_of_blood:"))
                    USER_HEALTH = USER_HEALTH+userPotion #Le joueur récupère des HP
                    SKIP_TURN=True #Permet de faire sauter un tour
                    NUMBER_OF_POTIONS -= 1
                else:
                    print("Vous n'avez plus de potions")

            case "-33":
                userAttack=0
                ennemyAttack = random.randint(5, 15)
                print("Vous avez sautés votre tour")
                print(emojis.encode(f"L'ennemi vous a infligé {ennemyAttack} HP :drop_of_blood:"))
                SKIP_TURN = False

    ENNEMY_HEALTH = ENNEMY_HEALTH-userAttack
    USER_HEALTH = USER_HEALTH - ennemyAttack
    print("-"*50)

if USER_HEALTH>0 and ENNEMY_HEALTH<=0:
    print(emojis.encode("Vous avez gagné :trophy:"))
elif USER_HEALTH<=0 and ENNEMY_HEALTH>0:
    print("Vous avez perdu")