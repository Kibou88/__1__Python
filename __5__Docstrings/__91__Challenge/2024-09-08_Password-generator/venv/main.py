# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-09-08
# Date de dernière modification: 2024-09-10
# ----------------------------------------------------------------
# version: 1.0
# -
# -------------------------------------------------------------------

# Appel des modules externes
from pathlib import Path
import random

# Appel des modules internes
from constantes import MOTS, MAJUSCULE, MINUSCULE, SYMBOLE, CHIFFRE, ALL_CHARACTERS, ALL_CHARACTERS_KANJIS

def password_1(MOTS: str) -> str:
    """
    Créer un mot de passe de niveau 1
    :param
    MOTS (lst): Liste contenant tout les mots les plus courants de la langue française
    :return:
    (str): Un mot aléatoire contenu dans la liste MOTS
    """
    return MOTS[random.randint(0,len(MOTS)-1)]

def password_2_3(level: int) -> str:
    """
    Créer un mot de passe de niveau 2 et 3
    :param
    level (int): Nombre de tour de la boucle pour choisir une letre MAJ, min, chiffre et symbole
    :return:
    password_generate (str): Mot de passe généré
    """
    random_alphadigit = [] # Stocker les différents caractères aléatoires
    random_alphadigit.append(MOTS[random.randint(0, len(MOTS) - 1)])

    for i in range(level):
        random_alphadigit.append(MINUSCULE[random.randint(0, len(MINUSCULE)-1)])
        random_alphadigit.append(MAJUSCULE[random.randint(0, len(MAJUSCULE)-1)])
        random_alphadigit.append(CHIFFRE[random.randint(0, len(CHIFFRE)-1)])
        random_alphadigit.append(SYMBOLE[random.randint(0, len(SYMBOLE)-1)])

    password_generate = ""
    for j in range(len(random_alphadigit)):
        index_choose = random.randint(0, len(random_alphadigit)-1)
        password_generate += random_alphadigit[index_choose]
        random_alphadigit.pop(index_choose)
    return password_generate

def password_4_5(number_character_min: int, number_character_max: int) -> str:
    """
    Créer un mot de passe de niveau 4 et 5
    :param
    number_character_min (int): Nombre de caractères minimum du mot de passe
    number_character_max (int): Nombre de caractères maximum du mot de passe
    :return:
    password_generate (str): Mot de passe généré
    """

    password_generate = ""

    if number_character_min == 16 and number_character_max == 32: # Mot de passe niveau 4
        for k in range(random.randint(number_character_min, number_character_max)):
            password_generate += ALL_CHARACTERS[random.randint(0, len(ALL_CHARACTERS)-1)]
        return password_generate

    elif number_character_min == 64 and number_character_max == 128: # Mot de passe niveau 5
        for l in range(random.randint(number_character_min, number_character_max)):
            password_generate += ALL_CHARACTERS_KANJIS[random.randint(0, len(ALL_CHARACTERS_KANJIS)-1)]
        return password_generate

def test_strong_password(user_password: str) -> str:
    """
    Permet de tester la robustesse d'un mot de passe utilisateur
    :param
    user_password (str): Mot de passe écrit par l'utilisateur
    :return:
    Affichage de différents print en fonction de la robustesse du mot de passe
    """

    count_min = 0
    count_maj = 0
    count_symbole = 0
    french_word_present = False

    for character_password in user_password:
        if character_password in MINUSCULE:
            count_min += 1
        elif character_password in MAJUSCULE:
            count_maj += 1
        elif character_password in SYMBOLE:
            count_symbole += 1

    for f in range(len(MOTS)):
        if MOTS[f] in user_password:
            french_word_present = True
            break

    if french_word_present and len(user_password) < 16:
        print("Votre mot de passe est faible")
    elif french_word_present and count_min >= 0 and count_maj >= 0 and count_symbole >= 0 \
            and len(user_password) >= 16:
        print("Votre mot de passe est moyen")
    elif not french_word_present and count_min > 0 and count_maj > 0 and count_symbole > 0 \
            and len(user_password) >= 64:
        print("Votre mot de passe est fort")


if __name__ == '__main__':
    print(f"mot_de_passe_1: {password_1(MOTS)}")
    print(f"mot_de_passe_2: {password_2_3(1)}")
    print(f"mot_de_passe_3: {password_2_3(3)}")
    print(f"mot_de_passe_4: {password_4_5(16, 32)}")
    print(f"mot_de_passe_5: {password_4_5(64, 128)}")

    test_strong_password(input("\nTester la force de votre mot de passe: "))