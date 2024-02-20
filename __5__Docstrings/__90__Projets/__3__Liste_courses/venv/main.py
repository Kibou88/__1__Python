# Liste des courses
# - Permettre à l'utilisateur d'ajouter/supprimer/afficher/vider une liste de course et de quitter le programme
# - Sauvegarder la liste des courses dans un JSON
###############################################################################################################
LISTECOURSE=[] # Variable global en MAJ par convenction
while True:
    print("Choississez parmi les 5 options suivantes:")
    print("1. Ajouter un élément dans la liste")
    print("2. Retirer un élément dans la liste")
    print("3. Afficher la liste")
    print("4. Vider la liste")
    print("5. Quitter")
    userChoice=input("Quel est votre choix? ")

    match userChoice:
        case "1": #Ajouter un élément
            food=input("Quel élément voulez-vous ajouter? ")

            if food.isalpha(): #Si ce n'est que du texte
                LISTECOURSE.append(food)
                print(f"L'élément {food} a bien été ajouté")
            else:
                print("L'élément n'est pas valide")

        case "2": #Retirer un élément
            for index, food in enumerate(LISTECOURSE,1): #Le chiffre '1' permet de commencer les index à 1
                print(f'{index}. {food}')

            indexUserChoice=input("Quel numéro voulez vous enlever? ")
            if indexUserChoice.isdigit():
                removeFood=LISTECOURSE.pop(int(indexUserChoice))
                print(f"L'élément {removeFood} a bien été retiré")
            else:
                pass

        case "3": #Afficher la liste
            if not LISTECOURSE==[]: #Si la liste n'est pas vide
                for index, food in enumerate(LISTECOURSE,1): #Le chiffre '1' permet de commencer les index à 1
                    print(f'{index}. {food}')
            else:
                print("La liste des courses est vide")

        case "4": #Vider la liste
            LISTECOURSE.clear()
            print("La liste des courses a été vidé")

        case "5": #Quitter le programme
            print("Bye")
            exit()

        case _: #Autre valeur tapée
            print("Ce choix n'est pas valide")

    print("_"*50)
