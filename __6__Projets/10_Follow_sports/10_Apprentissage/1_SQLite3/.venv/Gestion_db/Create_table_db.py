"""
Create table db
------------------------------
But:
---
Création des différentes tables dans un db
----------------------------------------------------------------------------
Date de création: 2026-04-20
Date de modification: 2026-05-06
----------------------------------------------------------------------------
Version V1:


"""
import os
import sqlite3
import sys

from class_colors import Colors

class Create_table:
    """
    Classe pour créer les différentes tables dans une db conforme au Cahier des Charges du projet
    """

    def __init__(self, dbName: str, tableName: str, typeTable: int, test=False):
        """
        Initialisation de la classe de création de tables.

        :param dbName (str): Nom de la base de données.
        :param tableName (str): Nom de la table.
        :param typeTable (int): Permet de choisir un type de table par rapport aux données voulues.
            N° table -> Titre de la table (nom des colonnes)
            0 -> Table Information Personnelle (prenom, age, taille_cm)
            1 -> Table Mensurations (date, poids_kg)
            2 -> Table Séances (id, date, exercices)
            3 -> Table Exercices (seance_id [foreign key], series, reps, charge_kg)
        :param test (bool): Permet de tester la classe seule.
            False -> La classe est utilisée par un autre programme
            True -> La classe est utilisée dans ce programme pour faire des tests de fonctionnement
        """
        


        self.dbName = dbName
        self.tableName = tableName
        self.test = test


        if (dbName == '' or tableName == ''):
            print("Aucune information envoye")
            sys.exit()
        with sqlite3.connect(self.dbName) as self.conn:
            self.cur = self.conn.cursor()

        match (typeTable):
            case 0:
                self.creation_table_personal_data()
                print("Table information personnelle creee")
            case 1:
                self.creation_table_mensurations()
                print("Table mensurations creee")
            case 2:
                self.creation_table_seances()
                print("Table seances creee")
            case 3:
                self.creation_table_exercices()
                print("Table exercices creee")

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
        if self.test:
            self.db_save_and_close()

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
        if self.test:
            self.db_save_and_close()

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
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {self.tableName} 
                                    (
                                        {", ".join(param_colonne)}
                                    )
                                ''')
        if self.test:
            self.db_save_and_close()

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
        if self.test:
            self.db_save_and_close()

    def db_save_and_close(self):
        """
        Sauvegarde et déconnexion de la db
        """
        self.conn.commit()
        self.conn.close()

if __name__ == "__main__":
    # Mettre test à True!!

    # ---------- Test OK ----------
    liste_name_table = ["informations_personnelles", "mensurations", "seances", "exercices"]
    dbName = "Test_template.db"

    for i in range(len(liste_name_table)):
        Create_table(dbName=dbName, tableName=liste_name_table[i], typeTable=i, test=True)

