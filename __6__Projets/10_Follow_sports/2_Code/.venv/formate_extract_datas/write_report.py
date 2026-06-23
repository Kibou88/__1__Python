"""
Ecriture du rapport
---------------------------
But:
Mettre en forme les informations de l'extraction et sauvegarder sous un txt
----------------------------------------------------------------------------
Date de création: 2026-06-19
Date de modification: 2026-06-19
----------------------------------------------------------------------------
Version PROTOTYPE:
"""

from extract_datas import Extract_datas
from pathlib import Path


class Write_report:
    """
    Génère un rapport texte à partir des données extraites d'une séance.

    Cette classe récupère les données extraites depuis la base, construit
    un contenu textuel structuré, puis l'enregistre dans un fichier .txt
    dans un dossier de sortie dédié.

    Attributes:
        database (str): Chemin de la base de données SQLite.
        report_contents (list): Contenu ligne par ligne du rapport.
        current_path (Path): Répertoire courant utilisé pour enregistrer le rapport.
        filename (str): Nom du fichier généré.
        dict_extract (dict): Données extraites utilisées pour construire le rapport.
    """

    def __init__(self, database: str, current_path: Path):
        """
        Initialise l'objet avec la base de données et le chemin de sortie.

        Args:
            database (str): Nom ou chemin de la base de données.
            current_path (Path): Répertoire courant de travail.
        """
        if database.endswith('.db'):
            self.database = database
            self.dict_extract = {}
        else:
            self.database = database + ".db"

        self.report_contents = []
        self.current_path = current_path

    def creation_file_name(self, j):
        """
        Construit le nom du fichier rapport à partir de la séance et des exercices.

        Le premier appel initialise le nom avec la date et le premier exercice,
        puis les appels suivants ajoutent les autres exercices.

        Args:
            j (int): Index de l'exercice dans la structure extraite.
        """
        if j == 0:
            self.filename = self.dict_extracted["date"] + "_" + self.dict_extracted['exercices'][0]['name']
        else:
            self.filename += "_" + self.dict_extracted['exercices'][j]['name']

    def create_txt_file(self):
        """
        Crée le fichier texte du rapport dans le dossier cible.

        Le fichier est ouvert en mode création exclusive pour éviter d'écraser
        un fichier déjà existant.
        """
        self.filename = self.filename.replace("/", "-")
        self.filename = self.filename + ".txt"
        path_filename = self.current_path / self.filename
        try:
            with open(path_filename, "x", encoding="utf-8") as file:
                for line in self.report_contents:
                    file.write(line)

        except FileExistsError:
            print("Fichier deja existant")

    def folder_to_save(self):
        """
        Prépare le dossier de sauvegarde du rapport.

        Crée un sous-dossier 'Rapport_seances' dans le répertoire courant
        s'il n'existe pas déjà.
        """
        self.current_path = self.current_path / "Rapport_seances"
        self.current_path.mkdir(parents=True, exist_ok=True)

    def dict_extract_datas(self):
        """
        Charge les données extraites depuis la base de données.

        Cette méthode stocke le dictionnaire retourné par la classe
        Extract_datas pour être réutilisé dans la génération du rapport.
        """
        self.dict_extracted = Extract_datas("tests.db").list_items_table_seances()

    def type_separator(self, type_sep):
        """
        Ajoute un séparateur de section au contenu du rapport.

        Args:
            type_sep (int): Type de séparateur à ajouter.
                1 pour une grande séparation, 2 pour une séparation simple.
        """
        if type_sep == 1:
            self.report_contents.append("\n==============================")
        elif type_sep == 2:
            self.report_contents.append(f"\n-----------------------------")

    def report_title(self):
        """
        Ajoute le titre principal du rapport.

        Le titre contient la date de la séance extraite.
        """
        self.report_contents.append(f"\tRapport du {self.dict_extracted['date']}")

    def report_exercices(self, j):
        """
        Ajoute le nom d'un exercice au rapport.

        Args:
            j (int): Index de l'exercice dans la liste des exercices extraits.
        """
        self.report_contents.append(f"\n- Exercice: {self.dict_extracted['exercices'][j]['name']}")

    def report_seances(self, i, j):
        """
        Ajoute une ligne décrivant une série d'exercice au rapport.

        Args:
            i (int): Index de la série dans l'exercice.
            j (int): Index de l'exercice dans la séance.
        """
        self.report_contents.append(f"\n\t* {self.dict_extracted['exercices'][j]['seances'][i]}")

    def process_write_report(self):
        """
        Lance le processus complet de génération du rapport.

        Récupère les données extraites, construit le contenu texte, crée le
        dossier de sortie puis écrit le fichier .txt final.
        """
        self.dict_extracted = Extract_datas(self.database).process_extract_seance()
        self.report_title()
        self.type_separator(1)
        for j in range(len(self.dict_extracted["exercices"])):
            self.report_exercices(j)
            self.creation_file_name(j)
            for i in range(len(self.dict_extracted['exercices'][j]['seances'])):
                self.report_seances(i, j)
            self.type_separator(2)
        print(self.report_contents)

        self.folder_to_save()
        self.create_txt_file()


if __name__ == "__main__":
    current_path = Path.cwd()
    Write_report("tests.db", current_path).process_write_report()