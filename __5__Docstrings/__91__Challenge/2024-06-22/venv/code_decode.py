# code-decode.py
# But:
# Contient les classes Phrase_Code et Phrase_Decode
# -----------------------------------
# Date de création: 2024-06-24
# Date de dernière modification: 2024-06-29
# ----------------------------------------------------------------
# version: 3.0
# - Combiner les 2 classes en 1 (V2)
# - Faire une méthode pour le codage, une pour le décodage et une autre pour gérer l'affichage en sortie (V2)
# - Docstrings corrigées avec la PEP257 (V3)
# - Suppression des 3 variables de classe dans __init__ (V3)
# -
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import PHRASE, CLEF

class CodageDecodage:
    """
    Permet d'effectuer un codage ou décodage symmétrique d'une phrase en fonction d'une clé
    :param:
    - clef(int): Clé de codage
    - phrase(str): Phrase à coder
    :return:
    - renvoie la phrase codée avec la méthode 'codage'
    - renvoie la phrase décodée avec la méthode 'décodage'
    """
    def __init__(self, clef: int, phrase: str):
        self.clef = clef
        self.phrase = phrase

    def codage(self):
        """
        Permet de coder la phrase:
            - Remplacement des espaces par des '_'
            - Rajout d'astérisk pour combler les espaces manquants en fin de phrase
            - Fais un codage symmétrique en fonction de la valeur de la clé
        :return:
            - phrase codée
        """
        phrase_code = ''
        phrase_out_space = self.phrase.replace(" ", "_")  # Remplacer les espaces par des "_"
        lignes = len(phrase_out_space) / self.clef
        while lignes != round(lignes, 0):  # Rajout "*" pour compléter l'espace vide à la fin de la phrase
            phrase_out_space += "*"
            lignes = len(phrase_out_space) / self.clef

        for ligne in range(self.clef):
            phrase_code += phrase_out_space[ligne::self.clef]

        return phrase_code

    def decodage(self, phrase_codee: str):
        """
        Permet de coder la phrase:
            - Fais un codage symmétrique en fonction de la valeur de la clé
            - Remplacement des espaces par des '_'
            - Rajout d'astérisk pour combler les espaces manquants en fin de phrase
        :return:
            - phrase codée
        """
        phrase_decode = ''
        lignes_decode = len(phrase_codee) / self.clef
        for ligne in range(int(lignes_decode)):
            phrase_decode += phrase_codee[ligne::int(lignes_decode)]

        phrase_space = phrase_decode.replace("_", " ")

        fin_chaine = (len(phrase_space) if phrase_space.find("*") == -1 else phrase_space.find("*"))
        return phrase_space[:fin_chaine:]

if __name__ == '__main__':
    cryptage = CodageDecodage(CLEF, PHRASE)
    phrase_cryptee = cryptage.codage()
    print("Voici la phrase codée: ", phrase_cryptee)

    phrase_decryptee = cryptage.decodage(phrase_cryptee)
    print("Voici la phrase décodée: ", phrase_decryptee)
