# Les chemins de fichiers sous WINDOWS
# - Apprendre à utiliser les chemins de fichiers via Python
# - Lire un fichier
############################################################

#chemin="C:\Users\thomas\desktop" # Ne fonctionne pas à cause de '\t'


chemin=r"C:\Users\thomas\desktop" # L'ajout de 'r' signifie prendre la chaine telle quelle
chemin_1="C:/Users/thomas/desktop" # ou inverser le sens des slashs
chemin_2="C:\\Users\\thomas\\desktop" # ou mettre double slash

chemin_file="C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__8__Les-fichiers\\fichier.txt"

f = open(chemin_file, "r") # r pour Read
print(f)
f.close() # Ferme le fichier

# Ferme le fichier à la fin de l'instruction
with open(chemin_file, 'r') as f:
    contenu = f.read()
    print(contenu)

with open(chemin_file, 'r') as f:
    contenu = repr(f.read()) # La fonction 'repr' permet d'accéder à la représentation de la chaîne de caractère
    # Apparation des '\n' représentant les sauts de lignes
    print(contenu)

with open(chemin_file, 'r') as f:
    contenu = f.readlines() # Va permettre de récupérer le fichier sous forme de liste
    #/!\Récupère aussi les tab, sauts de lignes, .../!\
    print(contenu)

with open(chemin_file, 'r') as f:
    contenu = f.read().splitlines() # Va récupérer le fichier sous forme de liste
    #/!\Sans le souci au dessus/!\
    print(contenu)