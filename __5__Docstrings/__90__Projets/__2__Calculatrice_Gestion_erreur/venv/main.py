# Calculatrice avec gestion erreur
# - But: Créer une calculatrice qui gère les erreurs de frappes de l'utilisateur
################################################################################
while True:
    print("Ecrire 'exit' dans un champ pour quitter le programme")
    nombre1 = input("Entrez le nombre 1: ")
    nombre2 = input("Entrez le nombre 2: ")

    if nombre1.isdigit() and nombre2.isdigit(): # Si nombre1 ET nombre2 sont des nombres
        nombre1=int(nombre1)
        nombre2=int(nombre2)
        print(f"La somme de {nombre1} et {nombre2} est {nombre2+nombre1}")
    elif nombre1.lower()=="exit" or nombre2.lower()=="exit":
        print("Au revoir")
        quit()
    else:
        print("Veuillez rentrer deux nombres valides")