"""
Test Gestion Base de données
------------------------------
But:
---
Création et gestion de tables BdD
----------------------------------------------------------------------------
Date de création: 2026-01-19
Date de modification: 2026-05-06
----------------------------------------------------------------------------
Version V1:
"""

import os
import sqlite3
import sys


from class_colors import Colors
from format_data import Format_data
from create_table_db import Create_table

class DataBase:
    """
    Classe contenant la création et la gestion de tables BdD
    """

    def __init__(self, dbName="default.db", data_to_send=""):
        """
        Initialisation de la classe BdD
        :param dbName (str): Nom de la DB. Si le nom ne contient pas l'extension '.db', il est rajouté.
        """
        if (data_to_send == "" or data_to_send == {} or data_to_send == []):
            print("Aucune donnee recue")
            sys.exit(1)

        self.data_to_send = data_to_send

        if not (dbName.endswith(".db")):
            dbName = dbName + ".db"
        elif dbName == "":
            dbName = "default.db"
        self.dbName = dbName

    def access_db(self):
        """
        Accéder à la base de donnée. Si absente, une base de donnée vide sera automatiquement créée
        """
        with sqlite3.connect(self.dbName) as self.conn:
            self.cur = self.conn.cursor()

    def db_save_and_close(self):
        """
        Sauvegarde et déconnexion de la db
        """
        self.conn.commit()
        self.conn.close()

    def request_write_data(self, table, row, fields):
        """
        Requête SQL pour l'écriture de donnée
        :param table (str): Nom de la table
        :param row (list): Liste des données à envoyée
        :param fields (str): Chaine de "?, " comportant le nombre de données à écrire
        :return:
        """
        if table == "seances":
            header_columns = "date, exercices"
        else:
            self.catch_id_key()
            row = list(row)
            row.insert(0, self.catch_id_key())
            header_columns = "seances_id, series, reps, loads_kg"

        query = f"INSERT INTO {table} ({header_columns}) VALUES ({fields})"
        self.cur.executemany(query, [row])
        self.conn.commit()  # Sauvegarde obligatoire !

    def check_or_create_table(self, table):
        """
        Verifie si la table n'est pas déjà créée, si il faut la créer la classe Create_table sera appellé
        :param table (str): Nom de la table
        """
        self.cur.execute(f"""SELECT name FROM sqlite_master WHERE type='table' AND name=?;""", (table,))
        tables = self.cur.fetchone()

        self.db_save_and_close()
        if not tables:
            if table == "seances":
                Create_table(dbName=self.dbName, tableName=table, typeTable=2)
            else: # type 3 si c'est une table exercice
                Create_table(dbName=self.dbName, tableName=table, typeTable=3)
        self.access_db()

    def catch_id_key(self):
        """
        Récupère la dernière valeur de l'ID (PRIMARY KEY) contenu dans la table "seances"
        :return: self.cur.fecthone()[0] (int): dernière valeur de l'ID (PRIMARY KEY)
        """
        self.cur.execute(f"""SELECT id FROM seances ORDER BY id DESC LIMIT 1;""")
        return self.cur.fetchone()[0]

    def process_to_write_data(self):
        """
        Méthode permettant l'écriture dans une base de donnée des données envoyées
        :return:
        """
        try:
            self.access_db()
            package_datas = Format_data(self.data_to_send).detect_type()
            for table, row, fields in package_datas:
                self.check_or_create_table(table)
                self.request_write_data(table, row, fields)
            self.db_save_and_close()
        except Exception as e:
            print(e)
            sys.exit(1)
        except PermissionError:
            print(f"Permissions insuffisantes pour acceder a {self.dbName}")
            sys.exit(1)

if __name__ == "__main__":
    test_datas2 = {
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
                            }
                        ]
                    }

    test_datas3 = {
        "date": "29/03/26",
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
    test2 = DataBase(dbName="test_manageDB2.db",data_to_send=test_datas2).process_to_write_data()
    test3 = DataBase(dbName="test_manageDB2.db", data_to_send=test_datas3).process_to_write_data()