from pprint import pprint
from Gestion.friend import FriendCleaner
from Gestion.library import Library

def main():
    library = Library()

    films = library.films()
    friends = FriendCleaner().list_from_data(library)

    print("Tous mes films")
    pprint(films)
    print()
    print("Tous mes ami:")
    pprint(friends)
    print()

    library.sort_by_type()
    film = library.get_random_choice()
    print(f"Film récupéré au hasard: {film}")
    print()

    films_lent = library.get_films_lent()
    print("J'ai prêté ces films:")
    pprint(films_lent)
    print()

    for film in films_lent:
        print(f"Le film '{film}' est chez", film.where)

if __name__ == "__main__":

    main()