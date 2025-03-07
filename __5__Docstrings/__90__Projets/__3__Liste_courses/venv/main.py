# Liste des courses
# - Permettre à l'utilisateur d'ajouter/supprimer/afficher/vider une liste de course et de quitter le programme
# - Sauvegarder la liste des courses dans un JSON
###############################################################################################################

def main():
    from gestion_JSON import lire_liste, ecrire_liste, remove_data_liste

    LISTECOURSE = []  # Variable global en MAJ par convenction
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
                    ecrire_liste(food)
                    print(f"L'élément {food} a bien été ajouté")
                else:
                    print("L'élément n'est pas valide")

            case "2": #Retirer un élément
                file_list = []
                file_list = lire_liste()
                if not file_list == []:  # Si le contenu du fichier JSON n'est pas vide
                    for index, food in enumerate(file_list, 1):  # Le chiffre '1' permet de commencer les index à 1
                        print(f'{index}. {food}')

                    indexUserChoice = input("Quel numéro voulez vous enlever? ")
                    if indexUserChoice.isdigit():
                        removeFood = file_list.pop(int(indexUserChoice)-1)
                        remove_data_liste(file_list)
                        print(f"L'élément {removeFood} a bien été retiré")

                else:
                    print("La liste des courses est vide")


            case "3": #Afficher la liste
                file_list=[]
                file_list=lire_liste()
                if not file_list==[]: #Si le contenu du fichier JSON n'est pas vide
                    for index, food in enumerate(file_list,1): #Le chiffre '1' permet de commencer les index à 1
                        print(f'{index}. {food}')
                else:
                    print("La liste des courses est vide")

            case "4": #Vider la liste
                LISTECOURSE.clear()
                remove_data_liste(LISTECOURSE)
                print("La liste des courses a été vidé")

            case "5": #Quitter le programme
                print("Bye")
                exit()

            case _: #Autre valeur tapée
                print("Ce choix n'est pas valide")

        print("_"*50)

if __name__ =="__main__":
    main()