from Components import *
from Tools import *

# Instancie un clou, une vis, un marteau, un tournevis et une caisse à outils
nail = Nail()
screw = Screw()
hammer = Hammer()
screwdriver = Screwdriver()
toolbox = ToolBox()
# On ajoute les outils dans la caisse avec la méthode "add_tool"
toolbox.add_tool(hammer)
toolbox.add_tool(screwdriver)

print("Voici les outils dans la caisse: ")
print(toolbox.tools)

# Serrez-la vis avec le tournevis.
# Affichez la vis avant après avoir été serrée.
print(screw)
screwdriver.tighten(screw)
print(screw)

# Enfoncez le clou avec le marteau.
# Affichez le clou avant et après avoir été enfoncé.
print(nail)
hammer.hammer_in(nail)
print(nail)

user_tool = input("Quel outil veux-tu enlever? ")
# La ligne dessous récupère la liste de toolbox.tools dans tool (un par un).
# "tool.__repr__()" représente la représentation textuelle de l'objet
# La condition si user_tool est dans tool.__repr__() pour chaque outil (tool) présent dans la boite à outils (toolbox.tools)
if user_tool in [tool.__repr__() for tool in toolbox.tools]:
    for tool in toolbox.tools:
        if user_tool in tool.__repr__():
            toolbox.remove_tool(tool)
            print(f"L'outil {user_tool} a été retiré de la caisse.")
            break

print("Voici les outils présents dans la caisse: ", toolbox.tools)


# repeindre le marteau
hammer.paint("yellow")
print(hammer)