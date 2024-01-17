class Film:
    """Film"""
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.where = None # L'attribut "where" permet de savoir où est le film

    def __str__(self): # utilisé pour fournir une représentation plus conviviale destinée à l'utilisateur.
        return f"{self.name} ({self.date})"

    def __repr__(self) -> str: # utile lorsque vous souhaitez fournir une représentation
        return str(self)       # détaillée et informative d'un objet pour le débogage ou la compréhension du code

class FilmVHF(Film):
    """Film VHF enfant de la classe Film"""

    type="vhf"
    def __init__(self, name, date):
        super().__init__(name, date)
        self.magnetic_tape = True

class FilmDVD(Film):
    """Film DVD enfant de la classe Film"""

    type="dvd"
    def __init__(self,name, date):
        super().__init__(name, date)
        self.mega_octets = 4700

class FilmCleaner:
    """Génère un film à partir des données brutes"""
    NAME_AND_DATE_INDEX = 0
    TYPE_INDEX = 1

    def __init__(self, film_data):
        self.film_data = film_data

    def generate(self):
        """Génère le film en appelant les autres méthodes"""
        name = self.generate_name()
        date = self.generate_date()
        type = self.generate_type()

    def generate_name(self):
        """Génère le nom du film"""
        name_date = self.film_data[self.NAME_AND_DATE_INDEX]
        return name_date[:name_date.index("(")].strip() # On récupère tout le nom du film qui est avant
        # la parenthèse

    def generate_date(self):
        """Génère la date du film"""
        date_letters = name_date[name_date.index("("):name_date.index(")")].strip()
        return int(date_letters)

    def generate_type(self):
        """Génère le type du film"""
        return self.film_data[self.TYPE_INDEX].lower()
