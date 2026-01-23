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

import sqlite3

class DataBase:
    """
    Classe contenant la création et la gestion de tables BdD
    """

    def __init__(self, dbName="default.db", dbTableName="default_table"):
        """
        Initialisation de la classe BdD
        :param dbName: Nom de la DB. Si le nom ne contient pas l'extension '.db', il est rajouté.
        :param dbTableName: Nom de la table
        """
        if(dbName.endswith(".db")):
            self.dbName = dbName
        else:
            self.dbName = dbName + ".db"

        self.dbTableName = dbTableName

    def create_column(self) -> str:
        """
        Demande à l'utilisateur le nombre de colonnes, ainsi que les noms et critères pour créer un nouvelle table
        :return: self.nom_table_colonne (str): retourne la forme concaténer des noms de colonnes et leurs critères
        """
        nombre_colonne = int(input("Nombre de colonne: "))
        self.liste_table_colonne = []
        for colonne in range(0, nombre_colonne):
            nom_colonne = input("Nom de la colonne + criteres: ")
            self.liste_table_colonne.append(nom_colonne)

        self.nom_table_colonne = ", ".join(self.liste_table_colonne)

    def create_table(self):
        """
        Créer une nouvelle table en fonction des paramètres de l'utilisateur.
        :param; self.dbTableName (str): nom de la table
        :param: self.nom_table_colonne (str): forme concaténer des noms de colonnes et leurs critères
        :return:
        """
        if (self.check_tables_exists()):
            self.create_column()
            with sqlite3.connect(self.dbName) as conn:  # Context manager auto-ferme
                cur = conn.cursor()
                cur.execute(f'''
                    CREATE TABLE {self.dbTableName} (
                        {self.nom_table_colonne}
                    )
                ''')
                conn.commit()

    def read_table(self):
        """
        Permet de lire la table et de récupérer les données souhaitées
        :param: self.dbTableName (str): nom de la table
        :return:
        """
        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()
            cur.execute(f'SELECT * FROM {self.dbTableName} ORDER BY annee')
            resultats = cur.fetchall()
            print(resultats)
            for livre in resultats:
                print(f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}")

    def show_tables(self)-> list:
        """
        Permet d'afficher les noms des différentes tables de la base de données
        :return: self.names_tables (list): noms des tables de la base de données
        """
        self.names_tables = []
        with sqlite3.connect(self.dbName) as conn:
            cur = conn.cursor()
            cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
            noms_tables = cur.fetchall()
            # print(noms_tables)
            self.names_tables=["".join(list(nom_table)) for nom_table in noms_tables]
            # print(self.names_tables)

    def check_tables_exists(self):
        """

        :return:
        """
        self.show_tables()
        if self.dbTableName not in self.names_tables:
            return True
        else:
            print(f"La table {self.dbTableName} existe deja")
            return False

if __name__ == "__main__":
    # db = DataBase("test", "test2")
    # db.create_table()
    db_test = DataBase("bibliotheque.db", "livres")
    # db_test.read_table()
    # db_test.show_tables()
    db_test.create_table()