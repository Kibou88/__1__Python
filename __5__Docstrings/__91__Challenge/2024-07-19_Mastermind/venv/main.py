# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-07-19
# Date de dernière modification: 2024-07-29
# ----------------------------------------------------------------
# version: 2.0
# - Variable 'coups' initialisée à 12 (V2)
# - Rassemblement en 1 print du message d'accueil (V2)
#-------------------------------------------------------------------

# Appel des modules externes

import random
# Appel des modules internes
from constantes import CARRE, PASTILLE, COLOR_TABLE


def game_message():
   """
   Présentation des règles du jeu et des commandes
   :return:
   N/A
   """
   print("JEU MASTERMIND\n"
         "Trouver la bonne combinaison de quatre couleurs secrètes que notre 'IA' aura généré.\n"
         "A chaque couleur bien positionnée, vous aure en retour un indicateur rouge\n"
         "A chaque couleur présente mais mal positionnée, vous aurez en retour un indicateur blanc\n"
         "Entrez votre combinaison secrète en utilisantes les chiffres des couleurs disponibles.\n"
         f"[1]:{COLOR_TABLE['YELLOW']} Jaune{COLOR_TABLE['WHITE']}\t"
         f"[2]:{COLOR_TABLE['BLUE']} Bleu{COLOR_TABLE['WHITE']}\t"
         f"[3]:{COLOR_TABLE['RED']} Rouge{COLOR_TABLE['WHITE']}\t"
         f"[4]:{COLOR_TABLE['GREEN']} Vert{COLOR_TABLE['WHITE']}\t"
         f"[5]:{COLOR_TABLE['WHITE']} Blanc{COLOR_TABLE['WHITE']}\t"
         f"[6]:{COLOR_TABLE['PURPLE']} Magenta{COLOR_TABLE['WHITE']}\t")

def comparaison_code(code_secret: list, liste_user: list) -> int:
    """
    Compare le code utilisateur et le code généré par l'IA et renvoie les infos de positionnement
    :param
    code_secret (list): Code généré par l'IA
    liste_user (list): Code entrée par l'utilisateur sous forme d'une liste
    :return:
    right_positioning (int): Nombre de couleurs bien placés
    wrong_positioning (int): Nombre de couleurs présentes dans le code mais mal placé
    """
    right_positioning = 0
    wrong_positioning = 0

    for number in range(len(liste_user)):
        if liste_user[number] == code_secret[number]:
            right_positioning += 1
        elif liste_user[number] in code_secret and liste_user[number] != code_secret[number]:
            wrong_positioning += 1

    return right_positioning, wrong_positioning

def result_message(liste_user: list):
    """
    Afficher les 4 carrés en fonction des couleurs choisies par l'utilisateur
    :param
    liste_user (list): Code entrée par l'utilisateur sous forme d'une liste
    :return:
    N/A
    """
    return "".join(
    f"{COLOR_TABLE[list(COLOR_TABLE)[liste_user[carre]-1]]}{CARRE} {COLOR_TABLE['WHITE']}"
    for carre in range(len(liste_user))
    )

if __name__ == '__main__':
   game_message()
   code_secret = random.sample(range(1, 7), 4)
   find_code = False
   coups = 12
   
   while not find_code:
       try:
           user_code = int(input("\nVeuillez saisir vos quatre chiffres pour les couleurs : "))
       except ValueError: # Si un caractère n'est pas un chiffre
           print("Votre saisie est incorrect...")
       else:
           # Convertion du type 'int' de user_code en 'list'
           liste_user = [int(i) for i in str(user_code)]
           right_positioning, wrong_positioning = comparaison_code(code_secret, liste_user)

           print(result_message(liste_user) + COLOR_TABLE['WHITE'] +
                 "Indicateurs:", COLOR_TABLE['RED'] + PASTILLE*right_positioning +
                 COLOR_TABLE['WHITE'] + PASTILLE*wrong_positioning)

           if right_positioning == 4:
               find_code = True

           coups -= 1
           print(f"Il vous reste {coups} coups")

           if coups == 0:
               print(f"Vous avez perdu. Le code secret était: {code_secret}")
               exit()

   print(f"Félicitation!! Vous avez trouvé le code secret en {coups} coups")