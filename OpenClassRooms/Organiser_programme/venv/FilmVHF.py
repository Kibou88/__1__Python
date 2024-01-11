from Film import Film

class FilmVHF(Film):
    """Classe Film VHF"""
    def __init__(self, name, created_date, place, type):
        super().__init__(name, created_date, place, type)
    
    def __repr__(self):
        """Représentation de l'objet"""
        "Le film VHF est {} de {} et est rangé {}".format(self.name, self.created_date, self.place)