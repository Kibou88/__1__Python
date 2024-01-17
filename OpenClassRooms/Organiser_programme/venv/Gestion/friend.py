from .data import friends

class Friend:
    """Classe Friend"""
    def __init__(self, name, film=None):
        self.name = name
        self.film = film
        if film: # Si film est "True", on attribue l'instance actuelle à l'attribut 'where' de
            film.where = self # l'objet "film"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()