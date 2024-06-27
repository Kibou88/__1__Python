# code-decode.py
# But:
# Contient les classes Phrase_Code et Phrase_Decode
# -----------------------------------
# Date de création: 2024-06-24
# Date de dernière modification: 2024-06-25
# ----------------------------------------------------------------
# version: 2.0
# - Combiner les 2 classes en 1
# - Faire une méthode pour le codage, une pour le décodage et une autre pour gérer l'affichage en sortie
#-------------------------------------------------------------------

# Appel des modules externes

# Appel des modules internes
from constantes import PHRASE, CLEF

class CodageDecodage():
    """
    Classe CodageDecodage:
    But: Permet d'effectuer un codage ou décodage symmétrique d'une phrase en fonction d'une clé
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

        self.phrase_out_space = ""
        self.phrase_code = ""
        self.phrase_decode = ""

    def codage(self):
        """
        Méthode codage:
        But: Permet de coder la phrase:
            - Remplacement des espaces par des '_'
            - Rajout d'astérisk pour combler les espaces manquants en fin de phrase
            - Fais un codage symmétrique en fonction de la valeur de la clé
        :return:
            - phrase codée
        """
        self.phrase_out_space = self.phrase.replace(" ", "_")  # Remplacer les espaces par des "_"
        self.lignes = len(self.phrase_out_space) / self.clef
        while self.lignes != round(self.lignes, 0):  # Rajout "*" pour compléter l'espace vide à la fin de la phrase
            self.phrase_out_space += "*"
            self.lignes = len(self.phrase_out_space) / self.clef

        for ligne in range(self.clef):
            self.phrase_code += self.phrase_out_space[ligne::self.clef]
            
        # print(f"Voici la phrase codée: {self.phrase_code}")
        return self.phrase_code

    def decodage(self, phrase_codee: str):
        """
        Méthode décodage:
        But: Permet de coder la phrase:
            - Fais un codage symmétrique en fonction de la valeur de la clé
            - Remplacement des espaces par des '_'
            - Rajout d'astérisk pour combler les espaces manquants en fin de phrase
        :return:
            - phrase codée
        """
        self.lignes_decode = len(phrase_codee) / self.clef
        for ligne in range(int(self.lignes_decode)):
            self.phrase_decode += phrase_codee[ligne::int(self.lignes_decode)]

        self.phrase_space = self.phrase_decode.replace("_", " ")

        self.fin_chaine = (len(self.phrase_space) if self.phrase_space.find("*") == -1 else self.phrase_space.find("*"))
        return self.phrase_space[:self.fin_chaine:]


if __name__ == '__main__':
    cryptage = CodageDecodage(CLEF, PHRASE)
    phrase_codee = cryptage.codage()
    print("Voici la phrase codée: ", phrase_codee)

    phrase_decodee = cryptage.decodage(phrase_codee)
    print("Voici la phrase décodée: ", phrase_decodee)
