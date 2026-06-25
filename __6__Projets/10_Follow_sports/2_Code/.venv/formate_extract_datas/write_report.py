"""
Ecriture du rapport
---------------------------
But:
Mettre en forme les informations de l'extraction et sauvegarder sous un txt
----------------------------------------------------------------------------
Date de création: 2026-06-19
Date de modification: 2026-06-24
----------------------------------------------------------------------------
Version PROTOTYPE:
"""
from pathlib import Path

from formate_extract_datas.extract_datas import ExtractDatas

from tools.log import Logs


class WriteReport:
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
        dict_extracted (dict): Données extraites utilisées pour construire le rapport.
        log (Logs): Gestionnaire de logs.
        error_to_main (bool): Indique qu'une erreur bloquante doit être remontée.
        warning_to_main (bool): Indique qu'un avertissement doit être remonté.
    """

    def __init__(self, database: str, current_path: Path, dict_extracted={},
                 log_name="Write_report", log_path=Path.cwd()/ "Test_log"):
        """
        Initialise l'objet avec la base de données, le dossier de sortie et les données optionnelles.

        Args:
            database (str): Nom ou chemin de la base de données.
            current_path (Path): Répertoire courant de travail.
            dict_extracted (dict, optional): Dictionnaire des données extraites.
                Defaults to {}.
            log_name (str, optional): Nom utilisé pour les logs. Defaults to "Extract_datas".
            log_path (Path, optional): Répertoire des logs. Defaults to Path.cwd() / "Test_log".
        """
        if database.endswith('.db'):
            self.database = database
            self.dict_extract = {}
        else:
            self.database = database + ".db"

        self.report_contents = []
        self.current_path = current_path
        self.dict_extracted = dict_extracted
        self.log = Logs(log_name=log_name, log_path=log_path)
        self.error_to_main = False
        self.warning_to_main = False


    def creation_file_name(self, j):
        """
        Construit progressivement le nom du fichier rapport.

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

        Returns:
            None: Le fichier est écrit sur disque et les logs sont mis à jour.
        """
        self.filename = self.filename.replace("/", "-")
        self.filename = self.filename + ".txt"
        path_filename = self.current_path / self.filename
        try:
            with open(path_filename, "x", encoding="utf-8") as file:
                for line in self.report_contents:
                    file.write(line)
            self.log.log_info(f"WRITE REPORT | Rapport {self.filename} cree")
        except FileExistsError:
            self.log.log_warning(f"WRITE REPORT | Rapport {self.filename} deja existant")
            self.warning_to_main = True

    def folder_to_save(self):
        """
        Prépare le dossier de sauvegarde du rapport.

        Crée un sous-dossier `Rapport_seances` dans le répertoire courant
        s'il n'existe pas déjà.

        Returns:
            None: Met à jour `self.current_path`.
        """
        self.current_path = self.current_path / "Rapport_seances"
        self.current_path.mkdir(parents=True, exist_ok=True)

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
        if self.dict_extracted['exercices'][j]['name'].count(" "):
            self.dict_extracted['exercices'][j]['name'] = self.dict_extracted['exercices'][j]['name'].replace(" ", "_")
        self.report_contents.append(f"\n- Exercice: {self.dict_extracted['exercices'][j]['name']}")

    def report_seances(self, i, j):
        """
        Ajoute une ligne décrivant une série d'exercice au rapport.

        Args:
            i (int): Ind1ex de la série dans l'exercice.
            j (int): Index de l'exercice dans la séance.
        """
        self.report_contents.append(f"\n\t* {self.dict_extracted['exercices'][j]['seances'][i]}")

    def process_write_report(self):
        """
        Lance le processus complet de génération du rapport.

        Si aucune donnée n'est déjà fournie, elles sont extraites depuis la base.
        Le contenu est ensuite formaté, le dossier de sortie est créé, puis le
        fichier texte est écrit sur disque.

        Returns:
            bool: Valeur de `self.warning_to_main`, indiquant si un avertissement
            a été détecté pendant la génération du rapport.
        """
        if self.dict_extracted == {}:
            self.dict_extracted, warning, error = ExtractDatas(self.database).process_extract_seance()
        self.report_title()
        self.type_separator(1)
        for j in range(len(self.dict_extracted["exercices"])):
            self.report_exercices(j)
            self.creation_file_name(j)
            for i in range(len(self.dict_extracted['exercices'][j]['seances'])):
                self.report_seances(i, j)
            self.type_separator(2)

        self.folder_to_save()
        self.create_txt_file()
        if self.warning_to_main:
            return self.warning_to_main

    def dict_extract_datas(self):
        """
        NON UTILISEE
        Charge les données extraites depuis la base de données.

        Cette méthode stocke le dictionnaire retourné par la classe
        `ExtractDatas` pour être réutilisé dans la génération du rapport.

        Returns:
            None: Met à jour `self.dict_extracted`.
        """
        self.dict_extracted = ExtractDatas("tests.db").list_items_table_seances()


if __name__ == "__main__":
    current_path = Path.cwd()
    warning = WriteReport("tests.db", current_path).process_write_report()
    if warning:
        print("Un warning a ete generee")