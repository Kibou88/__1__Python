"""
Test Gestion Base de données
------------------------------
But:
---
Tester la création et la gestion de tables BdD au travers d'une classe dédiée
----------------------------------------------------------------------------
Date de création: 2026-01-19
Date de modification: 2026-01-19
----------------------------------------------------------------------------
Version PROTOTYPE:


"""
import os
import sqlite3
import sys

from class_colors import Colors

class DataBase:
    """
    Classe contenant la création et la gestion de tables BdD
    """

    def __init__(self, dbName="default.db"):
        """
        Initialisation de la classe BdD
        :param dbName (str): Nom de la DB. Si le nom ne contient pas l'extension '.db', il est rajouté.
        """
        if not (dbName.endswith(".db")):
            dbName = dbName + ".db"
        elif dbName == "":
            dbName = "default.db"
        self.dbName = dbName

    def check_or_create_db(self):
        """
        Vérifie si la database demandée est présente, sinon création de la db.
        Ensuite, connexion à la db voulue
        :return:
        """
        try:
            self.conn = sqlite3.connect(self.dbName)
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)
            return False
        except PermissionError:
            print(f"Permissions insuffisantes pour acceder a {self.dbName}")
            return False


    def db_save_and_close(self):
        """
        Sauvegarde et déconnexion de la db
        :return:
        """
        self.conn.commit()
        self.conn.close()

    def nbre_interrogations(self):
        # ---- Fait correspondre le nombre de colonne avec le nombre de ? pour la requête SQL ----
        self.extract_colonne_name()


    def write_data(self, table_name, config_colonne, datas, foreign_key_activated):
        pass


if __name__ == "__main__":

    test_datas = ['27/03/26', 'squats fentes_avant']
    config_colonne = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                      "date TEXT NOT NULL",
                      "exercices TEXT NOT NULL"]
    name_colonne = ["date", "exercices"]

    test_datas2 = {
                        "date": "28/03/26",
                        "exercices": [
                            {
                                "name": "Squats",
                                "seance": [
                                    {
                                        "series": 10,
                                        "reps": 20,
                                        "loads": 30
                                    },
                                    {
                                        "series": 20,
                                        "reps": 30,
                                        "loads": 40
                                    }
                                ]
                            }
                        ]
                    }

    config_colonne2 = [
                    ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                      "date TEXT NOT NULL",
                      "exercices TEXT NOT NULL"],
                      ["seances_id INTEGER",
                       "series INTEGER NOT NULL",
                       "reps INTEGER NOT NULL",
                       "loads INTEGER",
                       "FOREIGN KEY (seances_id) REFERENCES seances (id)"]
                      ]


    name_colonne2 = [
                    ["date", "exercices"],
                    ["series", "reps", "loads"]
                    ]


    test_db = DataBase("Test")
    test_db.write_data(table_name="test",
                       config_colonne=config_colonne,
                       datas=test_datas,
                       foreign_key_activated=False)

