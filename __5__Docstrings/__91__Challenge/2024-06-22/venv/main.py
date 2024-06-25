# main.py
# But:
# Contient la logique du programme
# -----------------------------------
# Date de création: 2024-06-22
# Date de dernière modification: 2024-06-25
# ----------------------------------------------------------------
# version: 1.0
# -
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import PHRASE, CLEF
from code_decode import Phrase_Code, Phrase_Decode

def main():
    phrase_code = Phrase_Code(clef=CLEF, phrase=PHRASE)
    phrase_code = phrase_code.codage()

    phrase_decode = Phrase_Decode(clef=CLEF, phrase_codee=phrase_code)
    phrase_decode.shape_phrase_decodee()


if __name__ == '__main__':
    main()
