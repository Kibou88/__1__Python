# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-06-22
# Date de dernière modification: 2024-06-23
# ----------------------------------------------------------------
# version: 1.0
# -
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import PHRASE

clef = 6

print(len(PHRASE))
phrase_out_space = PHRASE.replace(" ", "_")
lignes = len(phrase_out_space)/6

while lignes != round(lignes, 0): #Rajout "*" pour compléter le tableau
    phrase_out_space += "*"
    lignes = len(phrase_out_space) / 6
print(lignes)

phrase_code = ""
#--------Test ok------------
for ligne in range(clef):
    phrase_code += phrase_out_space[ligne::clef]

print(phrase_code)
print(phrase_code == "S_i_adtajspprhle_opeou_iur_ntscreP*,ui_ny*")
#--------------------------------------------------------------------

lignes_decode = len(phrase_code) / clef
print(int(lignes_decode))

phrase_decode = ""
for ligne in range(int(lignes_decode)):
    phrase_decode += phrase_code[ligne::int(lignes_decode)]

print(phrase_decode)


if __name__ == '__main__':
   pass