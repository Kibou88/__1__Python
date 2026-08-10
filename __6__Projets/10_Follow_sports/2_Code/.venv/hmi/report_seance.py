"""
Report seance
------------------------------
But:
---
Afficher le compte-rendy de la séance sélectionné
----------------------------------------------------------------------------
Date de création: 2026-06-23
Date de modification: 2026-07-15
----------------------------------------------------------------------------
Version V1:

"""
import sys
from pathlib import Path
from pprint import pprint


class ReportSeance:
    """
    Construit et affiche un compte-rendu d'une séance à partir de données extraites.

    Cette classe transforme le dictionnaire de données d'une séance en une
    liste de lignes formatées, prête à être affichée ou réutilisée dans un rapport.

    Attributes:
        dict_extracted (dict): Données extraites contenant la date et les exercices.
        report_contents (list): Lignes formatées du compte-rendu.
    """

    def __init__(self, dict_extracted={}):
        """
        Initialise le rapport avec les données extraites de la séance.

        Args:
            dict_extracted (dict, optional): Dictionnaire contenant les données
                extraites. Doit contenir au minimum une date et une liste
                d'exercices.

        Raises:
            SystemExit: Si aucun dictionnaire valide n'est fourni.
        """
        if dict_extracted == {}:
            print("Aucune donnee envoyee")
            sys.exit(1)
        self.dict_extracted = dict_extracted
        self.report_contents = []

    def type_separator(self, type_sep):
        """
        Ajoute un séparateur de section au contenu du rapport.

        Args:
            type_sep (int): Type de séparateur à ajouter.
                1 pour une grande séparation, 2 pour une séparation simple.
        """
        if type_sep == 1:
            self.report_contents.append("==============================")
        elif type_sep == 2:
            self.report_contents.append(f"-----------------------------")

    def report_title(self):
        """
        Ajoute le titre principal du rapport.

        Le titre contient la date de la séance extraite.
        """
        self.report_contents.append(f"    Rapport du {self.dict_extracted['date']}")

    def report_exercices(self, j):
        """
        Ajoute le nom d'un exercice au rapport.

        Args:
            j (int): Index de l'exercice dans la liste des exercices extraits.
        """
        self.report_contents.append(f"- Exercice: {self.dict_extracted['exercices'][j]['name']}")

    def report_seances(self, i, j):
        """
        Ajoute une ligne décrivant une série d'exercice au rapport.

        Args:
            i (int): Index de la série dans l'exercice.
            j (int): Index de l'exercice dans la séance.
        """
        self.report_contents.append(f"    * {self.dict_extracted['exercices'][j]['seances'][i]}")

    def process_show_seance(self, test=False):
        """
        Construit le contenu complet du compte-rendu de séance.

        Le rapport est généré dans l'ordre: titre, exercices, puis lignes
        détaillées pour chaque série.

        Args:
            test (bool, optional): Si True, affiche le contenu ligne par ligne.
                Defaults to False.

        Returns:
            list: Liste des lignes composant le compte-rendu.
        """
        self.report_title()
        self.type_separator(1)
        for j in range(len(self.dict_extracted["exercices"])):
            self.report_exercices(j)
            for i in range(len(self.dict_extracted['exercices'][j]['seances'])):
                self.report_seances(i, j)
            self.type_separator(2)

        # if test:
        for line in self.report_contents:
            print(line)

        # return self.report_contents


if __name__ == "__main__":
    from formate_extract_datas.extract_datas import ExtractDatas

    dict_extracted = {
        'date': '16/06/2026',
        'exercices': [
            {'name': 'Biceps', 'seances': ['5 séries de 10 reps à 20.0 Kg']},
            {'name': 'Fentes avant', 'seances': ['5 séries de 10 reps à 11.0 Kg', '1 séries de 2 reps à 3.0 Kg']}
        ]
    }

    ReportSeance(dict_extracted).process_show_seance()