def shape_list_films_all(list_films, list_film_shaped):
    """Fonction pour réunir toutes les fonctions permettant la mise en forme de la liste de films
    Avant: "Name (created_date)", "type"
    Après: "Name", "created_date", "type" """
    created_date = []
    name = []
    type = []

    ligne_film_shaped = [name, created_date, type]
    for name_created, type_film in enumerate(list_films):
        name, created_date = separate_name_date(list_films, name_created, name, created_date)  # Fonction pour séparer le nom
        # de la date de création du film
        type = shape_type(list_films, name_created, type)  # Fonction pour mettre en forme le type
        list_film_shaped.append(ligne_film_shaped)

    return name, created_date, type

def shape_type(list_films, name_created, type):
    """Fonction pour mettre sous format MAJUSCULE les types"""
    type_film = list_films[name_created][1]
    type.append(type_film.upper())
    return type

def separate_name_date(list_films, name_created, name, created_date):
    """Fonction pour séparer le nom du film de la date de création"""
    full_info_film = list_films[name_created][0]
    name.append(full_info_film[0:len(full_info_film) - 7:1])  # Récupère le nom du film et supprime les espaces avant et après
    created_date.append(full_info_film[-5:-1:1])  # Récupère la date de création du film
    return name, created_date