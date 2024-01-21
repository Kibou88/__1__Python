class ToolBox:
    """Création de la classe Boite à outils"""

    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tools(self, tool):
        """Méthode pour retirer un outil dans la boite"""
        index = self.tools.index(tool)
        del self.tools[index]

    # """Méthode pour afficher la liste des outils dans la boite"""
        # def list_tools(self, tool):
        #     print("Voici la liste des outils:", self.tool)

class Hammer:
        """Création de la classe Marteau"""
        def __init__(self, color="red"):
            self.color = color

        def hammer_in(self, nail):
            """Méthode pour enfoncer un clou"""
            nail.nail_in()

        def hammer_out(self, nail):
            """Méthode pour retirer un clou"""
            nail.remove()

        def change_color(self, color):
            """Méthode pour changer la couleur du marteau"""
            self.color = color

        def __str__(self):
            """Méthode docstring représentaiton de l'objet"""
            return f"Le marteau est de couleur {self.color}"

class Screwdriver:
    """Création de la classe Tournevis"""
    def __init__(self, size=3):
        self.size = size

    def thighten(self, screw):
        """Méthode pour serrer une vis"""
        screw.tighten()

    def loosen(self, screw):
        """Méthode pour déserrer une vis"""
        screw.loosen() # Equivalent à Screw().loosen()

    def __str__(self):
        """Méthode docstring représentation de l'objet"""
        print("Le tournevis fait '{}'".format(self.size))

class Screw():
    """Création de la classe Vis"""

    MAX_TIGHTNESS = 5
    def __init__(self):
        """Initialisation du degré de serrage"""
        self.tighteness =0

    def tighten(self):
        """Vis sérrée"""
        if self.tighteness < 5:
            self.tighteness += 1


    def loosen(self):
        """Vis dévisser"""
        if self.tighteness >= 0:
            self.tighteness -= 1

    def __str__(self):
        """Retourne une forme visible de l'objet"""
        return "Vis avec un serrage de {}".format(self.tighteness)

class Nail():
    """Création de la classe Clou"""

    def __init__(self):
        self.in_wall = False # Initialisation: le clou n'est pas enfoncé dans le mur

    def nail_in(self):
        """Clou enfoncé"""
        if self.in_wall == False:
            self.in_wall = True
        else:
            print("The nail is already in the wall!")

    def remove(self):
        """Clou retiré"""
        if self.in_wall == True:
            self.in_wall = False
        else:
            print("The nail is out the wall!")

    def __str__(self):
        """Retourne une forme visible de l'objet"""
        wall_state = "In the wall" if self.in_wall else "Hors du mur"
        return wall_state
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# hammer_blue = Hammer("bleu") #Instanciation d'un marteau bleu
hammer = Hammer() #Instanciation d'un marteau rouge (par défaut)
screwdriver = Screwdriver() #Instanciation d'un tournevis de taille 3 (par défaut)
nail = Nail() #Instanciation d'un clou
screw = Screw() #Instanciation d'une vis

toolbox = ToolBox() #Instanciation de la boite à outils
# toolbox.add_tool(hammer) # Ajout du marteau rouge dans la boite à outils
# toolbox.add_tool(hammer_blue) # Ajout du marteau bleu dans la boite à outils
toolbox.add_tool(screwdriver) # Ajout du tournevis taille 3 dans la boite à outils

print("Etat du clou avant coup: ", nail)
hammer.hammer_in(nail)
print("Etat du clou après coup: ", nail)