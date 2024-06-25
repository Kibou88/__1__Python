# code-decode.py
# But:
# Contient les classes Phrase_Code et Phrase_Decode
# -----------------------------------
# Date de création: 2024-06-24
# Date de dernière modification: 2024-06-25
# ----------------------------------------------------------------
# version: 1.0
# -
#-------------------------------------------------------------------

class Phrase_Code():
    """
    Classe Phrase_Code:
    But: Permet d'effectuer un codage symmétrique d'une phrase en fonction d'une clé
    :param:
    - clef(int): Clé de codage
    - phrase(str): Phrase à coder
    :return:
    - renvoie la phrase codée
    """
    def __init__(self, clef: int, phrase: str):
        self.clef = clef
        self.phrase = phrase

        self.phrase_out_space = ""
        self.phrase_code = "" #Init de la variable contenant la phrase codée

    def prep_codage(self):
        """
        Méthode prep_codage:
        But: Permet de préparer la phrase à coder:
            - Remplacement des espaces par des '_'
            - Rajout d'astérisk pour combler les espaces manquants en fin de phrase
        :return:
            - phrase mis en forme
        """
        self.phrase_out_space = self.phrase.replace(" ", "_")  # Remplacer les espaces par des "_"
        lignes = len(self.phrase_out_space) / self.clef
        while lignes != round(lignes, 0):  # Rajout "*" pour compléter l'espace vide à la fin de la phrase
            self.phrase_out_space += "*"
            lignes = len(self.phrase_out_space) / self.clef
        # print(self.phrase_out_space)
        return self.phrase_out_space
    def codage(self):
        """
        Méthode codage:
        But: Permettre le codage de la phrase en fonction de la valeur de la clé
        :return:
            - Phrase codée
        """
        for ligne in range(self.clef):
            self.phrase_code += self.prep_codage()[ligne::self.clef]
        print(f"Voici la phrase codée: {self.phrase_code}")
        return self.phrase_code

#-------------------------------------------------------------------------------
class Phrase_Decode():
    """
        Classe Phrase_Decode:
        But: Permet d'effectuer un décodage symmétrique d'une phrase en fonction d'une clé (identique à celle de la phrase codée)
        :param:
        - clef(int): Clé de codage
        - phrase(str): Phrase à coder
        :return:
        - renvoie la phrase décodée
        """
    def __init__(self, clef: int, phrase_codee: str):
        self.clef = clef
        self.phrase_codee = phrase_codee

        self.phrase_decode = "" #Init de la variable contenant la phrase codée

    def decodage(self):
        """
        Méthode decodage
        But: Récupérer la phrase codée et la décodée
        :return:
        - Phrase décodée sans mise en forme
        """
        self.lignes_decode = len(self.phrase_codee) / self.clef
        for ligne in range(int(self.lignes_decode)):
            self.phrase_decode += self.phrase_codee[ligne::int(self.lignes_decode)]
        return self.phrase_decode

    def shape_phrase_decodee(self):
        """
        Méthode shape_phrase_decodee
        But: Remplace les '_' par des espaces et enlève les astériks (si besoin)
        :return:
        - Phrase décodée mis en forme
        """
        self.phrase_decode = self.decodage()
        self.phrase_space = self.phrase_decode.replace("_", " ")  # On remets les espaces

        fin_chaine = (len(self.phrase_space) if self.phrase_space.find("*") == -1 else self.phrase_space.find("*"))
        print("Voici la phrase décodée:", self.phrase_space[:fin_chaine:])
