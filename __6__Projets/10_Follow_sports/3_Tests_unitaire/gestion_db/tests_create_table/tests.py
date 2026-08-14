import unittest
import os
import sqlite3
import time
from unittest import TextTestRunner
from pathlib import Path
from datetime import datetime

from gestion_db.create_table import Create_table


def connect_db(db_file: str):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
    return conn, cursor

def close_db(conn):
    conn.close()

class Tests_create_table(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'test_db.db'
        self.path_db = Path(__file__).parent / self.db_name
        self.liste_name_table = ["informations_personnelles", "mensurations", "seances", "exercices"]
        self.empty_name = ''
        self.test = True
        self.log = "test_logs"
        file_log = datetime.now().strftime("%Y-%m-%d") + "_" + self.log + ".log"
        self.path_log = Path(__file__).parent / "Test_log" / file_log

    def tearDown(self) -> None:
        if self.path_db.exists():
            for _ in range(5):  # jusqu'à 5 tentatives
                try:
                    self.path_db.unlink()
                    break
                except PermissionError:
                    time.sleep(0.5)

        if self.path_log.exists():
            for _ in range(5):  # jusqu'à 5 tentatives
                try:
                    self.path_log.unlink()
                    break
                except PermissionError:
                    time.sleep(0.2)

    def test_db_empty_name(self):
        with self.assertRaises(ValueError) as context:
            Create_table(dbName=self.empty_name, test=self.test, log=self.log)
        self.assertEqual(str(context.exception), "aucun nom de DB envoye")

    def test_table_empty_name(self):
        with self.assertRaises(ValueError) as context:
            Create_table(dbName=self.db_name, test=self.test, log=self.log).creation_type_table(
                tableName=self.empty_name, typeTable=0)
        self.assertEqual(str(context.exception), "aucun nom de table envoye")

    def test_create_info_pers(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        conn_db = table_info_pers.creation_type_table(tableName=self.liste_name_table[0], typeTable=0)
        close_db(conn_db)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(informations_personnelles)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        # ---- Check bonnes créations des colonnes de la table ----
        self.assertEqual(types_colonnes["prenom"], "TEXT")
        self.assertEqual(types_colonnes["age"], "INTEGER")
        self.assertEqual(types_colonnes["taille_cm"], "INTEGER")
        # ---- Check présence du fichier log ----
        self.assertTrue(self.path_log.is_file())
        # ---- Check message du fichier log ----
        original_log_syntaxes = "| INFO | CREATE_TABLE | Table information personnelle creee"
        with open(self.path_log, "r") as f:
            self.assertIn(original_log_syntaxes, f.readline())
        conn.close()

    def test_create_mensurations(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        conn_db = table_info_pers.creation_type_table(tableName=self.liste_name_table[1], typeTable=1)
        close_db(conn_db)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(mensurations)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        # ---- Check bonnes créations des colonnes de la table ----
        self.assertEqual(types_colonnes["date"], "INTEGER")
        self.assertEqual(types_colonnes["poids_kg"], "INTEGER")
        # ---- Check présence du fichier log ----
        self.assertTrue(self.path_log.is_file())
        # ---- Check message du fichier log ----
        original_log_syntaxes = "| INFO | CREATE_TABLE | Table mensuration creee"
        with open(self.path_log, "r") as f:
            self.assertIn(original_log_syntaxes, f.readline())
        conn.close()

    def test_create_seances(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        conn_db = table_info_pers.creation_type_table(tableName=self.liste_name_table[2], typeTable=2)
        close_db(conn_db)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(seances)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        self.assertEqual(types_colonnes["id"], "INTEGER")
        self.assertEqual(types_colonnes["date"], "TEXT")
        self.assertEqual(types_colonnes["exercices"], "TEXT")
         # ---- Check présence du fichier log ----
        self.assertTrue(self.path_log.is_file())
        # ---- Check message du fichier log ----
        original_log_syntaxes = "| INFO | CREATE_TABLE | Table seances creee"
        with open(self.path_log, "r") as f:
            self.assertIn(original_log_syntaxes, f.readline())
        conn.close()

    def test_create_exercices(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        conn_db = table_info_pers.creation_type_table(tableName=self.liste_name_table[3], typeTable=3)
        close_db(conn_db)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(exercices)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        # ---- Check bonnes créations des colonnes de la table ----
        self.assertEqual(types_colonnes["seances_id"], "INTEGER")
        self.assertEqual(types_colonnes["series"], "INTEGER")
        self.assertEqual(types_colonnes["reps"], "INTEGER")
        self.assertEqual(types_colonnes["loads_kg"], "REAL")
        # ---- Check présence du fichier log ----
        self.assertTrue(self.path_log.is_file())
        # ---- Check message du fichier log ----
        original_log_syntaxes = "| INFO | CREATE_TABLE | Table exercices creee"
        with open(self.path_log, "r") as f:
            self.assertIn(original_log_syntaxes, f.readline())
        conn.close()


if __name__ ==  '__main__':
    unittest.main()

