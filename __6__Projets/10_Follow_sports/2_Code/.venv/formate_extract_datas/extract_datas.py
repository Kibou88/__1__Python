"""
Extraction des données
------------------------------
But:
---
Extraire les données de la base de données et les formatter.
----------------------------------------------------------------------------
Date de création: 2026-06-16
Date de modification: 2026-06-24
----------------------------------------------------------------------------
Version V1:
"""

import sqlite3
import os
from pathlib import Path

from tools.log import Logs


class ExtractDatas():
    """
    Extrait et formate les données de séances depuis une base SQLite.

    Cette classe ouvre une base de données, récupère les séances disponibles,
    permet d'en sélectionner une, puis reconstruit une structure de données
    exploitable contenant la date et la liste des exercices associés.

    Attributes:
        database (str): Chemin de la base de données SQLite.
        log_path (Path): Répertoire utilisé pour les logs.
        log (Logs): Instance de gestion des logs.
        dict_extract (dict): Dictionnaire final contenant les données extraites.
        error_to_main (bool): Indique qu'une erreur bloquante doit être remontée.
        warning_to_main (bool): Indique qu'un avertissement doit être remonté.
        resultats_seances (list): Résultat de la requête sur les séances.
        user_selection (str): Identifiant de séance choisi par l'utilisateur.
        conn: Connexion SQLite active.
        cur: Curseur SQLite utilisé pour exécuter les requêtes.
    """

    def __init__(self, database: str, log_name="Extract_datas", log_path=Path.cwd()/ "Test_log"):
        """
        Initialise l'objet avec le chemin de la base de données et le système de log.

        Si le nom fourni ne se termine pas par `.db`, l'extension est ajoutée
        automatiquement.

        Args:
            database (str): Nom ou chemin de la base de données.
            log_name (str, optional): Nom du log utilisé pour tracer l'exécution.
                Defaults to "Extract_datas".
            log_path (Path, optional): Répertoire des logs.
                Defaults to Path.cwd() / "Test_log".
        """
        if database.endswith('.db'):
            self.database = database
        else:
            self.database = database + ".db"

        self.dict_extract = {}
        self.log_path = log_path
        self.log = Logs(log_name=log_name, log_path=log_path)
        self.error_to_main = False
        self.warning_to_main = False

    def check_db_exist(self):
        """
        Vérifie que la base de données existe dans le répertoire attendu.

        Returns:
            bool: True si la base existe, False sinon.
        """
        self.path_db = self.log_path.parent / self.database
        if not self.path_db.is_file():
            return False
        return True

    def check_selection_int(self):
        """
        Vérifie que la sélection utilisateur correspond à un entier.

        La méthode repose sur `self.user_selection` et redemande une sélection
        tant que la valeur saisie n'est pas numérique.

        Returns:
            None: Met à jour `self.warning_to_main` et relance la saisie si besoin.
        """
        while not self.user_selection.isdigit():
            self.warning_to_main = True
            self.log.log_warning(f"EXTRACT_DATAS | L'utilisateur a saise la valeur {self.user_selection}")
            self.menu_choix_seance()

    def format_data(self, nom_table):
        """
        Formate un nom de table en libellé lisible.

        Remplace les underscores par des espaces, puis met la première lettre
        en majuscule.

        Args:
            nom_table (str): Nom brut de la table.

        Returns:
            str: Nom formaté pour l'affichage.
        """
        if nom_table.count("_"):
            nom_table = nom_table.replace("_", " ")

        return nom_table.capitalize()

    def menu_choix_seance(self):
        """
        Affiche les séances disponibles et demande à l'utilisateur d'en choisir une.

        La liste affichée provient de `self.resultats_seances`.

        Returns:
            None: Stocke la valeur saisie dans `self.user_selection`.
        """
        os.system('cls')
        print("Listes des seances:")
        for seance in self.resultats_seances:
            print(f"id: {seance[0]}, date: {seance[1]}, exercices: {seance[2]}")
        self.user_selection = input("Choix de la seance: ")

    def listes_exos(self, liste_exo_data):
        """
        Récupère les exercices associés à la séance sélectionnée.

        Pour chaque table d'exercice, interroge la base avec l'identifiant de
        séance choisi, puis construit une structure descriptive pour l'export.

        Args:
            liste_exo_data (list): Liste des tables d'exercices à interroger.
        """
        try:
            for table_exo in liste_exo_data:
                dict_exercices = {}
                self.cur.execute(
                    f"SELECT * FROM {table_exo} WHERE seances_id = {int(self.user_selection)}"
                )

                listes_seance = self.cur.fetchall()
                dict_exercices["name"] = self.format_data(table_exo)
                dict_exercices["seances"] = []

                for index, seance in enumerate(listes_seance):
                    dict_exercices["seances"].append(
                        f"{seance[1]} séries de {seance[2]} reps à {seance[3]} Kg"
                    )

                self.dict_extract["exercices"].append(dict_exercices)
        except sqlite3.OperationalError:
            self.error_to_main = True
            self.log.log_error(
                f"EXTRACT_DATA | Erreur lors de la récupération des exercices pour la séance: "
                f"{self.user_selection}"
            )

    def process_extract_seance(self):
        """
        Lance le processus complet d'extraction d'une séance.

        Ouvre la base, charge toutes les séances, demande une sélection,
        récupère la date correspondante, puis extrait les exercices associés.

        Returns:
            tuple: `(dict_extract, warning_to_main, error_to_main)`.
        """
        if not (self.check_db_exist()):
            self.error_to_main = True
            self.log.log_error(f"EXTRACT_DATAS | La base de donnee {self.database} n'existe pas")
            self.log.log_error(f"EXTRACT_DATAS | Path de la base de donnee: {self.path_db}")
        else:
            try:
                with sqlite3.connect(self.database) as self.conn:
                    self.cur = self.conn.cursor()
                    self.cur.execute("SELECT * FROM seances ORDER BY id")
                    self.resultats_seances = self.cur.fetchall()
                    self.menu_choix_seance()
                    self.check_selection_int()

                    self.dict_extract["date"] = str(self.resultats_seances[int(self.user_selection) - 1][1])
                    self.dict_extract["exercices"] = []

                    liste_exo_data = list(self.resultats_seances[int(self.user_selection) - 1])[2].split(" ")
                    self.listes_exos(liste_exo_data)
            except sqlite3.OperationalError:
                self.error_to_main = True
                self.log.log_error(
                    f"EXTRACT_DATAS | Impossible de se connecter a la base de donnees {self.database}"
                )
                self.conn.close()

        return self.dict_extract, self.warning_to_main, self.error_to_main

    def list_all_tables(self):
        """
        Affiche toutes les tables présentes dans la base de données.

        Cette méthode est non utilisée dans le code actuel.

        Returns:
            None
        """
        self.connexion()
        self.cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
        tables = self.cur.fetchall()
        print("Tables de la bd: ", tables)
        self.db_save_and_close()


if __name__ == "__main__":
    test, error, warning = ExtractDatas("tests.db").process_extract_seance()
    print("Output:\n", test)