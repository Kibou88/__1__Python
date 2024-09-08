# test.py
# But:
# Module pour tester des fonctions du code
# -----------------------------------

from constantes import *

phrase_code = ''
sentence_without_space = PHRASE.replace(" ", "_")
total_lenght = len(sentence_without_space)
split_sentence = total_lenght / CLEF
print(CLEF)
print(total_lenght)
print(int(round(split_sentence,0)))
lenght_sentence_stars = CLEF * int(round(split_sentence,0)) - total_lenght
sentence_without_space += "*" * lenght_sentence_stars
print(sentence_without_space)