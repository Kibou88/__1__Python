# Compter les occurences
# - Fonction "count"
##########################################

test = "Bonjour le jour"
print("Test avec 'jour': ", test.count("jour")) # Retourne 2
print("Test avec ' jour': ", test.count(" jour")) # Retourne 1

### Dans le 1er cas, le programme va chercher littéralement tout les suites de caractères
### correspondant à 'jour' => donc il y a "bonJOUR" et le mot 'jour'
### Dans le 2nd cas, il va chercher les suites de caractères 'jour' avec un espace mis devant
### et là, on retrouve bien notre mot 'jour' compter 1 fois