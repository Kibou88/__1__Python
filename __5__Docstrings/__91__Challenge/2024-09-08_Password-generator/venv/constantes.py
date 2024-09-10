# constantes.py
# But:
# Contient les constantes du code
# -----------------------------------
# Date de création: 2024-09-08
# Date de dernière modification: 2024-09-10
# ------------------------------------------
# version: 1.0
# -
#-------------------------------------------

# Appel des modules externes
from pathlib import Path
import string
import unicodedata

file_mots = Path.cwd() / "input" / "mots.txt"

with open(file_mots, "r", encoding='utf-8') as f:
    MOTS = f.read().split(" ")

MINUSCULE = string.ascii_lowercase
MAJUSCULE = string.ascii_uppercase
CHIFFRE = string.digits
SYMBOLE = string.punctuation

ALL_CHARACTERS = MINUSCULE + MAJUSCULE + CHIFFRE + SYMBOLE

# -------------------KANJIS UNICODE---------------------------
KANJI_UNICODE_HEXA_MIN = 0x2F30
KANJI_UNICODE_HEXA_MAX = 0x2F40

KANJIS = ""
for i in range(KANJI_UNICODE_HEXA_MIN, KANJI_UNICODE_HEXA_MAX):
    KANJIS += chr(i)

ALL_CHARACTERS_KANJIS = ALL_CHARACTERS + KANJIS


if __name__ == '__main__':
    print(KANJIS)