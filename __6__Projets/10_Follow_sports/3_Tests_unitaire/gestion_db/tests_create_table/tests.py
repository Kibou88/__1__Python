import unittest
import os
import sqlite3
from unittest import TextTestRunner
from pathlib import Path
from datetime import datetime

from gestion_db.create_table import Create_table

def connect_db(db_file: str):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    return conn, cursor

class Tests_create_table(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'test_db.db'
        self.liste_name_table = ["informations_personnelles", "mensurations", "seances", "exercices"]
        self.empty_name = ''
        self.test = True
        self.log = "test_logs"
        file_log = datetime.now().strftime("%Y-%m-%d") + "_" + self.log + ".log"
        self.path_log = Path(__file__).parent / "Test_log" / file_log
        self.nb_test = 6

    def tearDown(self):
        if self.nb_test == 2:
            print("Fin du test")
        else:
            print("Test suivant")
        self.nb_test -= 1

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
        table_info_pers.creation_type_table(tableName=self.liste_name_table[0], typeTable=0)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(informations_personnelles)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        assert types_colonnes["prenom"] == "TEXT"
        assert types_colonnes["age"] == "INTEGER"
        assert types_colonnes["taille_cm"] == "INTEGER"

    def test_create_mensurations(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        table_info_pers.creation_type_table(tableName=self.liste_name_table[1], typeTable=1)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(mensurations)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        assert types_colonnes["date"] == "INTEGER"
        assert types_colonnes["poids_kg"] == "INTEGER"

    def test_create_seances(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        table_info_pers.creation_type_table(tableName=self.liste_name_table[2], typeTable=2)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(seances)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        assert types_colonnes["id"] == "INTEGER"
        assert types_colonnes["date"] == "TEXT"
        assert types_colonnes["exercices"] == "TEXT"

    def test_create_exercices(self):
        table_info_pers = Create_table(dbName=self.db_name, test=self.test, log=self.log)
        table_info_pers.creation_type_table(tableName=self.liste_name_table[3], typeTable=3)
        conn, cur = connect_db(db_file=self.db_name)
        cur.execute("PRAGMA table_info(exercices)")
        types_colonnes = {colonne[1]: colonne[2] for colonne in cur.fetchall()}
        assert types_colonnes["seances_id"] == "INTEGER"
        assert types_colonnes["series"] == "INTEGER"
        assert types_colonnes["reps"] == "INTEGER"
        assert types_colonnes["loads_kg"] == "REAL"

    def test_check_presence_log_file(self):
        self.assertTrue(self.path_log.is_file())

    def test_check_logs(self):
        original_log_syntaxes = [
            "| ERROR | CREATE_TABLE | Aucun nom de Database envoye",
            "| ERROR | CREATE_TABLE | Aucun nom de table envoye",
            "| INFO | CREATE_TABLE | Table information personnelle creee",
            "| INFO | CREATE_TABLE | Table mensuration creee",
            "| INFO | CREATE_TABLE | Table seances creee",
            "| INFO | CREATE_TABLE | Table exercices creee"
        ]
        with open(self.path_log, "r") as f:
            lignes = f.read().splitlines()
        for log_syntax in original_log_syntaxes:
            correct_syntax = False
            for ligne in lignes:
                print(log_syntax)
                print(ligne)
                print("\n")
                if log_syntax in ligne:
                    correct_syntax = True
                    break
                # print(correct_syntax)
            self.assertTrue(correct_syntax)


if __name__ == '__main__':
    unittest.main()

