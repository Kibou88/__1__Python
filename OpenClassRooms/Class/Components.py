class Screw:
    """Vis."""
    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0
    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1
    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""
    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False
    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True
    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False
    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."