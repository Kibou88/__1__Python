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

class FriendCleaner(Friend):
    """Classe Friend Cleaner enfant de Friend"""
    NAME_INDEX=0
    FILM_INDEX=1

    def __init__(self):
        self.friends = friends

    def generate(self, data, library):
        """Retourne un ami à partir des données brutes"""
        name = data[self.FILM_INDEX]
        if len(data) > 1:
            film_name = date[self.FILM_INDEX]
            film = library.find_by_name(film_name)
        else:
            film = None
        return Friend(name, film)

    def list_from_data(self, library):
        """Retourne une liste d'amis à partir des données brutes

        Attributs:
            - library => une instance de bibliothèque de films"""
        result=[]
        for data in self.friends:
            friend = self.generate(data, library)
            result.append(friend)
        return result