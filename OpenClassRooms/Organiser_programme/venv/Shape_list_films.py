def shape_list_films_all(list_films):
    """Fonction pour réunir toutes les fonctions permettant la mise en forme de la liste de films
    Avant: "Name (created_date)", "type"
    Après: "Name", "created_date", "type" """
    separate_name_age(list_films)

def separate_name_age(list_films):
    """Fonction pour séparer le nom de la date de création du film"""
    for name_created, type in enumerate(list_films):
        full_info_film = list_films[name_created][0]
        type = list_films[name_created][1]
        print(f"Valeur de name_created: {full_info_film}")
        print(f"Valeur de type {type}")
        created_date = []
        # for film in full_info_film:
        created_date = full_info_film[-5:-1:1] # Récupère la date de création du film
        print(f"Le film {full_info_film} a été créé le {created_date}")