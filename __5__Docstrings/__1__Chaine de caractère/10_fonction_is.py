# Vérifier et analyser les chaînes de caractères
# - Fonction "is"
##########################################

######### RENVOI FALSE SI 1 ELEMENT DE LA CHAINE EST FAUX ############
test = "bonjour"
test_2 = "Bonjour"
test_3 = "50a"
test_4 = "50"

print("test est en minuscule: ", test.islower()) # Est-ce que test est en minuscule
print("test_2 est en minuscule: ", test_2.islower()) # Est-ce que test_2 est en minuscule
print("test_3 est numérique:", test_3.isdigit()) # Est-ce que test_3 est un nombre
print("test_4 est numérique:", test_4.isdigit()) # Est-ce que test_4 est un nombre