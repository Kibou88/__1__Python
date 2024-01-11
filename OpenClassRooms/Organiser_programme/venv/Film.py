# from abc import ABC

class Film:
    """Classe Film
    Classe Abstraite"""
    def __init__(self, name, created_date, place, type):
        self.name = name
        self.created_date = created_date
        self.place = place
        self.type = type
    
    def random_choice(self):
        """Méthode pour choisir un film au hasard"""
        pass