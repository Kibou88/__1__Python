class ToolBox:
    """Boite à outils."""
    def __init__(self):
        """Initialise les outils."""
        self.tools = []
    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)
    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]


class Screwdriver:
    """Tournevis."""
    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size
    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()
    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""
    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color
    def paint(self, color):
        """Paint le marteau."""
        self.color = color
    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()
    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()
    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"