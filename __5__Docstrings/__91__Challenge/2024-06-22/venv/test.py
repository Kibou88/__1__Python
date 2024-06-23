# test.py
# But:
# Module pour tester des fonctions du code
# -----------------------------------

from constantes import *

print(len(PHRASE))
phrase_out_space = PHRASE.replace(" ", "_")
lignes = len(phrase_out_space)/6

while lignes != round(lignes, 0):
    phrase_out_space += "*"
    lignes = len(phrase_out_space) / 6
print(phrase_out_space)