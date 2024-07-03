# code-decode.py
# But:
# Contient les classes Phrase_Code et Phrase_Decode
# -----------------------------------
# Date de création: 2024-06-24
# Date de dernière modification: 2024-07-02
# ----------------------------------------------------------------
# version: 4.2
# - Combiner les 2 classes en 1 (V2)
# - Faire une méthode pour le codage, une pour le décodage et une autre pour gérer l'affichage en sortie (V2)
# - Docstrings corrigées avec la PEP257 (V3)
# - Suppression des 3 variables de classe dans __init__ (V3)
# - Simplification de la méthode codage (V4.1)
# - Simplification de la méthode décodage (V4.2)
# - Correction de la méthode codage (V5)
# - Ajout du module math pour arrondir au supérieur (V5)
#-------------------------------------------------------------------

# Appel des modules externes
import math
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
        total_lenght = len(self.phrase) / self.clef
        missing_stars = self.clef * int(math.ceil(total_lenght)) - len(self.phrase)
        sentence_to_code = f"{self.phrase.replace(' ', '_')}{'*' * missing_stars}"

        return "".join(sentence_to_code[ligne::self.clef] for ligne in range(self.clef))

    def decodage(self, sentence_coded: str):
        """
        Permet de coder la phrase:
            - Fais un codage symmétrique en fonction de la valeur de la clé
            - Remplacement des espaces par des '_'
            - Rajout d'astérisk pour combler les espaces manquants en fin de phrase
        :return:
            - phrase codée
        """
        segment_numbers = int(len(sentence_coded) / self.clef)
        sentence_shaped = \
            "".join(sentence_coded[ligne::segment_numbers] for ligne in range(segment_numbers))

        ending_sentence = \
            (len(sentence_coded) if sentence_shaped.find("*") == -1 else sentence_shaped.find("*"))

        sentence_decoded = sentence_shaped.replace("_", " ")

        return sentence_decoded[:ending_sentence:]

    def __str__(self):
        return "Voici la phrase codée: " + self.codage() + \
            "\nVoici la phrase décodée: " + self.decodage(sentence_coded)

if __name__ == '__main__':
    cryptage = CodageDecodage(CLEF, PHRASE)
    sentence_coded = cryptage.codage()

    sentence_decoded = cryptage.decodage(sentence_coded)

    print(str(cryptage))