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

from pathlib import Path

from tools.class_colors import Colors
from tools.log import Logs
from formate_extract_datas.formate_datas import Format_data
from gestionDB.create_table import Create_table

class DataBase:
    """
    Classe contenant la création et la gestion de tables BdD
    """

    def __init__(self, dbName="default.db", data_to_send={}, log_name="Manage_database",
                 log_path=Path.cwd()/ "Test_log", test=False):
        """
        Initialisation de la classe BdD
        :param dbName (str): Nom de la DB. Si le nom ne contient pas l'extension '.db', il est rajouté.
        :param data_to_send (dict): Données à envoyer à la db sous format dict
        :param log_path (str): Chemin vers le dossier des logs
        :param test (bool): Utiliser pour les tests. False à défaut
        """
        if (data_to_send == "" or data_to_send == {} or data_to_send == []):
            print("Aucune donnee recue")
            self

        if not (dbName.endswith(".db")):
            dbName = dbName + ".db"
        elif dbName == "":
            dbName = "default.db"

        self.dbName = dbName
        self.data_to_send = data_to_send
        self.log_name = log_name
        self.log_path = log_path
        self.log = Logs(log_name=log_name, log_path=log_path)
        self.error_to_main = False
        self.test=test

        if (data_to_send == "" or data_to_send == {} or data_to_send == []):
            print("Aucune donnee recue")
            self.log.log_error("Aucune donnee recue")
            self.error_to_main = True
            if self.test:
                raise ValueError ("Aucune donnee recue")

        if not (dbName.endswith(".db")):
            dbName = dbName + ".db"
        elif dbName == "":
            self.log.log_warning("Aucun nom pour la db reçue. Nom par défaut: default.db")
            dbName = "default.db"
            if self.test:
                raise ValueError ("Aucun nom pour la db reçue")

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
                (Create_table(dbName=self.dbName, log_name=self.log_name, log_path=self.log_path)
                 .creation_type_table(tableName=table, typeTable=2))
            else: # type 3 si c'est une table exercice
                (Create_table(dbName=self.dbName, log_name=self.log_name, log_path=self.log_path)
                 .creation_type_table(tableName=table, typeTable=3))
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
            # with sqlite3.connect(self.dbName) as self.conn:
            #     self.cur = self.conn.cursor()

            package_datas, error_prep_data = Format_data(self.data_to_send, log_name=self.log_name,
                                                         log_path=self.log_path).detect_type()
            # temp = package_datas
            # for table, row, fields in temp:
            #     print(table, row, fields)
            for table, row, fields in package_datas:
                # print(table, row, fields)
                self.check_or_create_table(table)
                self.request_write_data(table, row, fields)
            self.conn.close()

        except Exception as e:
            print(e)
            self.log.log_error(f"MANAGE_DATABASE | Erreur survenue: {e}")
            self.error_to_main = True
            self.conn.close()

        except PermissionError:
            print(f"Permissions insuffisantes pour acceder a {self.dbName}")
            self.log.log_error(f"MANAGE_DATABASE | Permissions insuffisantes pour acceder a {self.dbName}")
            self.error_to_main = True
            self.conn.close()
        return self.error_to_main

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
    error2 = DataBase(dbName="test_manageDB2.db",data_to_send=test_datas2).process_to_write_data()
    error3 = DataBase(dbName="test_manageDB2.db", data_to_send=test_datas3).process_to_write_data()