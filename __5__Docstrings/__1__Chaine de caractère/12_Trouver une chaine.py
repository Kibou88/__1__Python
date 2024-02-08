# Compter les occurences
# - Fonction "find"
# - Fonction "index"
##########################################

test = "Bonjour le jour"
print("Test avec index: ", test.index("jour")) # Retourne 3: nbre de caractère jusqu'au 'j' en partant de 0
print("Test avec find: ", test.find("jour")) # Retourne 3

print("Test avec find et le mot 'soir': ", test.find("soir")) # Retourne -1 => Aucune correspondance
print("Test avec index et le mot 'soir': ", test.index("soir")) # Lèves une ValueError

print("Test avec rfind: ", test.rfind("jour")) # On part à droite de la fin de la chaine
