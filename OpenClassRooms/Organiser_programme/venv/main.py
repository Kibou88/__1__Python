from Listes_films_friends import list_films, list_friends
from Shape_list_films import shape_list_films_all

def main():
    films = []
    friends = []
    films = list_films()
    user = list_friends()
    list_film_shaped = shape_list_films_all(films)


if __name__ == "__main__":
    main()