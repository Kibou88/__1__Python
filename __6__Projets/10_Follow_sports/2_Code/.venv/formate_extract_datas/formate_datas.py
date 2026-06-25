"""
Formatage des données
------------------------------
But:
---
Vérifier les données utilisateurs et les formater pour qu'elles soient insérées dans la base de données
----------------------------------------------------------------------------
Date de création: 2026-01-24
Date de modification: 2026-06-24
----------------------------------------------------------------------------
Version V1:
"""

import sys
import sqlite3
from pathlib import Path

from tools.log import Logs


class Format_data:
    """
    Vérifie, trie et formate des données pour préparer des requêtes SQL.

    Cette classe oriente les données selon leur type d'entrée, transforme
    un dictionnaire de séance en données exploitables pour l'insertion en base,
    et génère le nombre de placeholders SQL nécessaires.

    Attributes:
        test (bool): Indique si la classe est en mode test.
        data (list | tuple | dict): Données d'entrée à formater.
        log (Logs): Gestionnaire de logs.
        error_to_main (bool): Indique qu'une erreur bloquante doit être remontée.
        list_exo_seance (list): Liste des exercices formatés pour la séance.
        list_datas (list): Liste des tuples de données à insérer.
        list_tables (list): Liste des tables SQL associées.
        list_nb_fields (list): Liste du nombre de champs SQL par ligne.
        zip_tables_data_fields (zip): Regroupement table, données et placeholders.
    """

    def __init__(self, data: (list or tuple or dict), log_name="Formate_datas", log_path=Path.cwd()/ "Test_log",
                 test=False):
        """
        Initialise l'objet avec les données à formater et le système de log.

        Args:
            data (list | tuple | dict): Données à traiter.
            log_name (str, optional): Nom utilisé pour les logs. Defaults to "Formate_datas".
            log_path (Path, optional): Répertoire des logs. Defaults to Path.cwd() / "Test_log".
            test (bool, optional): Active l'affichage de contrôle. Defaults to False.
        """
        self.test = test
        self.data = data
        self.log = Logs(log_name=log_name, log_path=log_path)
        self.error_to_main = False

    def detect_type(self: (dict or list or tuple)) -> zip:
        """
        Détecte le type de données reçues et appelle la méthode adaptée.

        Si les données sont un dictionnaire, elles sont formatées avec
        `format_dico()`. Si elles sont une liste ou un tuple, elles sont
        envoyées vers `format_liste_tuple()`.

        Returns:
            tuple[zip, bool] | None: Couple contenant l'association des tables,
            des données et des champs, ainsi que le flag d'erreur si l'entrée est
            un dictionnaire et que le mode test est désactivé.
        """
        if type(self.data) == dict:
            self.format_dico()
            if not self.test:
                return self.zip_tables_data_fields, self.error_to_main
        elif type(self.data) == list or type(self.data) == tuple:
            self.format_liste_tuple()
        else:
            self.log.log_error(f"FORMAT DATA | Format {type(self.data)} non pris en charg")
            print(f"Format {type(self.data)} non pris en charge")
            return self.zip_tables_data_fields, self.error_to_main

    def format_dico(self) -> zip:
        """
        Formate un dictionnaire de données de séance pour l'insertion SQL.

        Construit la liste des tables, des données et du nombre de champs
        attendus pour chaque requête d'insertion.

        Returns:
            None: Les résultats sont stockés dans les attributs de l'instance.
        """
        self.list_exo_seance = []
        self.list_datas = []
        self.list_tables = []
        self.list_nb_fields = []

        try:
            self.list_tables.append("seances")
            for i in range(len(self.data["exercices"])):
                self.list_exo_seance.append((self.data["exercices"][i]["name"]).lower().replace(" ", "_"))

                for j in range(len(self.data["exercices"][i]["seance"])):
                    self.list_tables.append(self.data["exercices"][i]["name"].lower().replace(" ", "_"))
                    self.list_datas.append((
                        self.data["exercices"][i]["seance"][j]["series"],
                        self.data["exercices"][i]["seance"][j]["reps"],
                        self.data["exercices"][i]["seance"][j]["loads"]
                    ))

            self.list_datas.insert(0, (self.data["date"], " ".join(self.list_exo_seance)))
            self.list_nb_fields = [self.nbre_interro(self.list_tables[i], self.list_datas[i])
                                   for i in range(len(self.list_datas))]
            self.zip_tables_data_fields = zip(self.list_tables, self.list_datas, self.list_nb_fields)
        except Exception:
            self.log.log_error(f"FORMAT DATA | Une erreur est survenue pour le formatage du dictionnaire:")
            self.log.log_error(f"FORMAT DATA | {self.data}")
            self.error_to_main = True

        if self.test:
            for table, row, nb_fields in self.zip_tables_data_fields:
                print(table, row, nb_fields)

    def format_liste_tuple(self):
        """
        Formate des données fournies sous forme de liste ou de tuple.

        Cette méthode est prévue mais pas encore implémentée.

        Returns:
            None: Fonction vide pour l'instant.
        """
        pass
        # print("Format liste ou tuple")

    def nbre_interro(self, table_name: str, fields: int) -> str:
        """
        Génère la chaîne de placeholders SQL nécessaires pour une ligne.

        Pour la table `seances`, le nombre de `?` correspond au nombre de champs
        de la ligne. Pour les autres tables, un champ supplémentaire est prévu
        pour la clé étrangère `seances_id`.

        Args:
            table_name (str): Nom de la table cible.
            fields (int): Nombre de champs à insérer.

        Returns:
            str: Chaîne SQL du type `?, ?, ?`.
        """
        if not (table_name == "seances"):
            interrogations = "?, " * (len(fields) + 1)
        else:
            interrogations = "?, " * len(fields)
        return interrogations[:-2]

    def format_date(self):
        """
        Formate une date selon le format attendu par la base.

        Cette méthode est prévue mais pas encore implémentée.

        Returns:
            None: Fonction vide pour l'instant.
        """
        pass


if __name__ == "__main__":
    list_datas = [('28/03/26', 'squats fentes_avant'), ("5", "10", "15")]
    dict_datas = {
        "date": "28/03/26",
        "exercices": [
            {
                "name": "Squats",
                "seance": [
                    {
                        "series": 10,
                        "reps": 20,
                        "loads": 30.5
                    },
                    {
                        "series": 20,
                        "reps": 30,
                        "loads": 40.0
                    }
                ]
            },
            {
                "name": "Fentes avant",
                "seance": [
                    {
                        "series": 10,
                        "reps": 20,
                        "loads": 35
                    }
                ]
            }
        ]
    }
    int_datas = 10

    test_dict_datas = Format_data(dict_datas, test=True).detect_type()

    test2_dict_datas, erreur = Format_data(dict_datas).detect_type()
    print("------------------------------")
    print("Test 2:")
    for table, row, nb_fields in test2_dict_datas:
        print(table, row, nb_fields)