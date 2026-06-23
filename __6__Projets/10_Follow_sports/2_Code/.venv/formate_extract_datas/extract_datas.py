"""
Extraction des données
------------------------------
But:
---
Extraire les données de la base de données et les formatter.
----------------------------------------------------------------------------
Date de création: 2026-06-16
Date de modification: 2026-06-19
----------------------------------------------------------------------------
Version PROTOTYPE:
"""

import sqlite3


class Extract_datas:
    """
    Extrait et formate les données de séances depuis une base SQLite.

    Cette classe ouvre une base de données, récupère les séances disponibles,
    permet d'en sélectionner une, puis reconstruit une structure de données
    exploitable contenant la date et la liste des exercices associés.

    Attributes:
        database (str): Chemin de la base de données SQLite.
        dict_extract (dict): Dictionnaire final contenant les données extraites.
        user_selection (str): Identifiant de séance choisi par l'utilisateur.
        conn: Connexion SQLite active.
        cur: Curseur SQLite utilisé pour exécuter les requêtes.
    """

    def __init__(self, database: str):
        """
        Initialise l'objet avec le chemin de la base de données.

        Si le nom fourni ne se termine pas par `.db`, l'extension est ajoutée
        automatiquement.

        Args:
            database (str): Nom ou chemin de la base de données.
        """

        if database.endswith('.db'):
            self.database = database
        else:
            self.database = database + ".db"

        self.dict_extract = {}

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

    def menu_choix_seance(self, resultats_seances):
        """
        Affiche les séances disponibles et demande à l'utilisateur d'en choisir une.

        Args:
            resultats_seances (list): Liste des séances récupérées depuis la base.
        """

        print("Listes des seances:")
        for seance in resultats_seances:
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
        for table_exo in liste_exo_data:
            dict_exercices = {}
            self.cur.execute(
                f"SELECT * FROM {table_exo} WHERE seances_id = {int(self.user_selection)}"
            )

            listes_seance = self.cur.fetchall()
            print("Liste des exos: ", listes_seance)
            dict_exercices["name"] = self.format_data(table_exo)
            dict_exercices["seances"] = []

            for index, seance in enumerate(listes_seance):
                dict_exercices["seances"].append(
                    f"{seance[1]} séries de {seance[2]} reps à {seance[3]} Kg"
                )

            self.dict_extract["exercices"].append(dict_exercices)

    def process_extract_seance(self):
        """
        Lance le processus complet d'extraction d'une séance.

        Ouvre la base, charge toutes les séances, demande une sélection,
        récupère la date correspondante, puis extrait les exercices associés.

        Returns:
            dict: Dictionnaire contenant la date et la liste des exercices.
        """
        with sqlite3.connect(self.database) as self.conn:
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT * FROM seances ORDER BY id")
            resultats_seances = self.cur.fetchall()
            self.menu_choix_seance(resultats_seances)

            self.dict_extract["date"] = str(resultats_seances[int(self.user_selection) - 1][1])
            self.dict_extract["exercices"] = []

            liste_exo_data = list(resultats_seances[int(self.user_selection) - 1])[2].split(" ")
            print("Listes des exos1: ", liste_exo_data)
            self.listes_exos(liste_exo_data)

        return self.dict_extract

    def list_all_tables(self):
        """
        Affiche toutes les tables présentes dans la base de données.

        Cette méthode est indiquée comme non utilisée dans le code actuel.

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
    test = Extract_datas("tests.db").process_extract_seance()
    print("Output:\n", test)