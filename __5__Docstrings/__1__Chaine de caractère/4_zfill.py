# Manipuler les chaines de caractères part 4
# - Remplir les zéros
##########################################

############## FONCTIONNE UNIQUEMENT SUR LES CHAINES DE CARACTERES ##############
######################### CONVERTIR LES NOMBRES EN STR #########################
test = "9"
test2 = "10"    
test1 = test.zfill(4) # Le chiffre représente la longueur qu'il y aura au final
test2 = test2.zfill(4)

print("Test 1 avec 9:", test1)
print("Test 2 avec 10:", test2)