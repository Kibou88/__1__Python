# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-07-19
# Date de dernière modification: 2024-08-01
# ----------------------------------------------------------------
# version: 4.0
# - Variable 'coups' initialisée à 12 (V2)
# - Rassemblement en 1 print du message d'accueil (V2)
# - Fonction 'game_message' renvoie le texte d'accueil (V3)
# - Condition du while qui change (V3)
# - Ajout d'une condition pour faire apparaître le nombre de coups restants (V3)
# - Modification du code suite passage 'COLOR_TABLE' en tuple
#-------------------------------------------------------------------

# Appel des modules externes

import random
# Appel des modules internes
from constantes import CARRE, PASTILLE, COLOR_TABLE


def game_message():
   """
   Présentation des règles du jeu et des commandes
   :return:
   (str): Renvoie le texte d'accueil
   """
   return "JEU MASTERMIND\n" \
         "Trouver la bonne combinaison de quatre couleurs secrètes que notre 'IA' aura généré.\n" \
         "A chaque couleur bien positionnée, vous aurez en retour un indicateur rouge\n" \
         "A chaque couleur présente mais mal positionnée, vous aurez en retour un indicateur blanc\n" \
         "Entrez votre combinaison secrète en utilisantes les chiffres des couleurs disponibles.\n" \
         f"[1]:{COLOR_TABLE[0]} Jaune{COLOR_TABLE[4]}\t" \
         f"[2]:{COLOR_TABLE[1]} Bleu{COLOR_TABLE[4]}\t" \
         f"[3]:{COLOR_TABLE[2]} Rouge{COLOR_TABLE[4]}\t" \
         f"[4]:{COLOR_TABLE[3]} Vert{COLOR_TABLE[4]}\t" \
         f"[5]:{COLOR_TABLE[4]} Blanc{COLOR_TABLE[4]}\t" \
         f"[6]:{COLOR_TABLE[5]} Magenta{COLOR_TABLE[4]}\t"

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
    f"{COLOR_TABLE[carre-1]}{CARRE} {COLOR_TABLE[4]}"
    for carre in liste_user
    )

if __name__ == '__main__':
   print(game_message())
   code_secret = random.sample(range(1, 7), 4)
   coups = 12
   right_positioning = 0
   
   while not right_positioning == 4:
       try:
           user_code = int(input("\nVeuillez saisir vos quatre chiffres pour les couleurs : "))
       except ValueError: # Si un caractère n'est pas un chiffre
           print("Votre saisie est incorrect...")
       else:
           # Convertion du type 'int' de user_code en 'list'
           liste_user = [int(i) for i in str(user_code)]
           right_positioning, wrong_positioning = comparaison_code(code_secret, liste_user)

           print(result_message(liste_user) + COLOR_TABLE[4] +
                 "Indicateurs:", COLOR_TABLE[2] + PASTILLE*right_positioning +
                 COLOR_TABLE[4] + PASTILLE*wrong_positioning)

           if right_positioning != 4:
               coups -= 1
               print(f"Il vous reste {coups} coups")

           if coups == 0:
               print(f"Vous avez perdu. Le code secret était: {code_secret}")
               exit()

   print(f"Félicitation!! Vous avez trouvé le code secret en {coups} coups")