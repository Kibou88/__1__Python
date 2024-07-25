from constantes import COLOR_TABLE
print("grg"*5)
liste_color_table = list(COLOR_TABLE)
user_code = int(input("\nVeuillez saisir vos quatre chiffres pour les couleurs : "))
liste_user = [int(i) for i in str(user_code)]

for index, nom in enumerate(liste_user, 1):
    print(f"{COLOR_TABLE['BLUE']}Index: {index} {COLOR_TABLE['WHITE']}et nom: {nom}")