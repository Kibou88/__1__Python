# test.py
# But:
# Module pour tester des fonctions du code
# -----------------------------------

from constantes import *
phrase_space = "Salut, je suis ici pour apprendre Python****"
fin_chaine = (len(phrase_space) if phrase_space.find("*") == -1 else phrase_space.find("*"))
phrase = phrase_space[:fin_chaine:]
print(phrase)
print(phrase_space.find("*"))