from Listes_films_friends import list_films, list_friends
from Shape_list_films import shape_list_films_all
from IHM import IHM_all

def main():
    choice = IHM_all() # Fonction pour afficher l'IHM et permettre à l'utilisateur de faire des choix
    list_film_shaped = shape_list_films_all(films, list_film_shaped) # Fonction pour mettre en forme les listes

    match choice:
        case "1":
            # Liste des films par nom
            pass
        case "2":
            # Liste des films par date de création
            pass
        case "3":
            # Liste des films par type
            pass
        case "4":
            # Film au hasard
            pass
        case "5":
            # Savoir quel(s) film(s) sont chez des amis
            pass
if __name__ == "__main__":
    #____Initialisation des variables_____
    films = []
    friends = []
    list_film_shaped = []
    # Fonctions pour mettre tout les films dans une liste
    films = list_films()
    user = list_friends()

    while True:
        main()