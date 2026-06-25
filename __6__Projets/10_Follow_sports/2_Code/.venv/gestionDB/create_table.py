"""
Create table db
------------------------------
But:
---
Création des différentes tables dans un db
----------------------------------------------------------------------------
Date de création: 2026-04-20
Date de modification: 2026-06-24
----------------------------------------------------------------------------
Version V2.3:
- Ajout de la méthode creation_type_table (V2)
- Ajout du raise ValueError pour les tests (test=True) pour vérifier la présence de nom pour dbName et tableName (V2.1)
- Ajout du return conn dans la méthode creation_type_table pour fermer la bd lors des tests uniquement + suppression des éléments inutiles (V2.2)
- Modification "log" par "log_name" dans __init__ (V2.3)

"""
import os
import sqlite3
import sys
from pathlib import Path

from tools.class_colors import Colors
from tools.log import Logs


class Create_table:
    """
    Classe pour créer les différentes tables dans une db conforme au Cahier des Charges du projet
    """

    def __init__(self, dbName: str, test=False, log_name="Create_table", log_path = Path.cwd()/ "Test_log"):
        """
        Initialisation de la classe de création de tables.

        :param dbName (str): Nom de la base de données.
        :param test (bool): Permet de tester la classe seule.
            False -> La classe est utilisée par un autre programme
            True -> La classe est utilisée dans ce programme pour faire des tests de fonctionnement
        """
        self.dbName = dbName
        self.test = test
        self.log = Logs(log_name=log_name, log_path=log_path, test=test)
        self.error_to_main = False
        self.warning_to_main = False

        if (dbName == ''):
            self.log.log_error(f"CREATE_TABLE | Aucun nom de Database envoye")
            if not test: # Si test à False, on quitte
                sys.exit(1)
            elif test:
                self.log.close_log()
                raise ValueError("aucun nom de DB envoye")


    def creation_type_table(self, tableName: str, typeTable: int):
        """
        Permet de choisir définir le type de table et son nom à créer dans la db
        :param tableName (str): Nom de la table.
        :param typeTable (int): Permet de choisir un type de table par rapport aux données voulues.
            N° table -> Titre de la table (nom des colonnes)
            0 -> Table Information Personnelle (prenom, age, taille_cm)
            1 -> Table Mensurations (date, poids_kg)
            2 -> Table Séances (id, date, exercices)
            3 -> Table Exercices (seance_id [foreign key], series, reps, charge_kg)
        """
        if (tableName == ''):
            self.log.log_error(f"CREATE_TABLE | Aucun nom de table envoye")
            # if not self.test: # Si test à False, on quitte
            #     sys.exit(1)
            self.error_to_main = True
            if self.test:
                self.log.close_log()
                raise ValueError("aucun nom de table envoye")
                
        self.tableName = tableName

        with sqlite3.connect(self.dbName) as self.conn:
            self.cur = self.conn.cursor()

        match (typeTable):
            case 0:
                self.creation_table_personal_data()
                self.log.log_info(f"CREATE_TABLE | Table information personnelle creee")
                print("Table information personnelle creee")
            case 1:
                self.creation_table_mensurations()
                self.log.log_info(f"CREATE_TABLE | Table mensuration creee")
                print("Table mensurations creee")
            case 2:
                self.creation_table_seances()
                self.log.log_info(f"CREATE_TABLE | Table seances creee")
                print("Table seances creee")
            case 3:
                self.creation_table_exercices()
                self.log.log_info(f"CREATE_TABLE | Table exercices creee")
                print(f"Table exercice {tableName} creee")

        if self.test:
            self.log.close_log()
            return self.conn

    def creation_table_personal_data(self):
        """
        Création de la table informations personnelles.

        Colonnes -> Attributs
        prenom -> TEXT
        age -> INTEGER
        taille_cm -> INTEGER
        """
        param_colonne = ["prenom TEXT", "age INTEGER", "taille_cm INTEGER"]
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName} 
                            (
                                {", ".join(param_colonne)}
                            )
                        ''')

    def creation_table_mensurations(self):
        """
        Création de la table mensurations.

        Colonnes -> Attributs
        date -> INTEGER
        poids_kg -> INTEGER
        """
        param_colonne = ["date INTEGER", "poids_kg INTEGER"]
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName} 
                                    (
                                        {", ".join(param_colonne)}
                                    )
                                ''')

    def creation_table_seances(self):
        """
        Création de la table séances.

        Colonnes -> Attributs
        id -> INTEGER PRIMARY KEY AUTOINCREMENT
        date -> TEXT NOT NULL
        exercices -> TEXT NOT NULL
        """
        param_colonne = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
                         "date TEXT NOT NULL",
                         "exercices TEXT NOT NULL"]
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS seances 
                                    (
                                        {", ".join(param_colonne)}
                                    )
                                ''')

    def creation_table_exercices(self):
        """
        Création de la table exercices.

        Colonnes -> Attributs
        seances_id -> INTEGER (FOREIGN KEY: récupère l'id de la table seances)
        series -> INTEGER NOT NULL
        reps -> REAL NOT NULL
        loads_kg -> REAL (virgule)
        """
        param_colonne = ["seances_id INTEGER",
                         "series INTEGER NOT NULL",
                         "reps INTEGER NOT NULL",
                         "loads_kg REAL",
                         "FOREIGN KEY (seances_id) REFERENCES seances(id)"]
        self.cur.execute("PRAGMA foreign_keys = ON;")
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName} 
                            (
                                {", ".join(param_colonne)}
                            )
                        ''')

    


if __name__ == "__main__":
    # Mettre test à True!!

    # ---------- Test OK ----------
    liste_name_table = ["informations_personnelles", "mensurations", "seances", "exercices"]
    dbName = "Test_template.db"

    creation_table = Create_table(dbName=dbName, test=True, log="Create_table")
    for i, name_table in enumerate(liste_name_table):
        creation_table.creation_type_tabe(tableName=name_table, typeTable = i)

    fail_creation_table = Create_table(dbName="", test=True, log="Create_table")
    fail_creation_table2 = Create_table(dbName=dbName, test=True, log="Create_tabley")
    fail_creation_table2.creation_type_tabe(tableName='', typeTable = 1)
