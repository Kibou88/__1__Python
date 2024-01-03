class Film:
    """Classe Film

    Prends le nom du film en paramètre
    Méthode watch: voir le film"""
    def __init__(self, name):
        self.name = name

    def watch(self):
        """Méthode pour voir le film"""
        print("Bon visionnage de {}".format(self.name))

class FilmCassette(Film):
    """Classe enfant FilmCassette de Film

    Récupère le nom du film dans la classe parent
    Prends le paramètre magnetic_tape
    """
    def __init__(self,name, magnetic_tape = "K7"):
        self.name = name
        self.magnetic_tape = magnetic_tape

    def rewind(self):
        """Méthode pour rembobiner le film"""
        if self.magnetic_tape == "K7": # Si c'est bien une K7 => on peut rembobiner
            print("La cassette {} se rembobine".format(self.name))
        else: # Sinon on passe
            print("Le film {} n'est pas une cassette. C'est un {}!!".format(self.name, self.magnetic_tape))

film = Film("2001: L'Odyssée de l'espace") # Instancie le film: 2001 l'Odyssée de l'espace
film_cassette = FilmCassette("Blade runner") # Instancie le film cassette: Blade runner
film_cassette2 = FilmCassette("Star Trek", "DVD") # Instancie le film cassette: Star Trek avec ajout DVD

film.name = "Star Wars" # On change la valeur de name
film.watch()

# film_cassette.name
film_cassette.watch()
film_cassette.rewind()

film_cassette2.watch()
film_cassette2.rewind()