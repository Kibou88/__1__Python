"""
Extract Base de Données
---------------------------
But:
Extraire les données d'une table et les afficher
"""
import sqlite3

class Extract_datas():

    def __init__(self, database: str):
        if database.endswith('.db'):
            self.database = database

        else:
            self.database = database + ".db"

        self.dict_extract = {}


    def menu_choix_seance(self, resultats_seances):
        print("Listes des seances:")
        for seance in resultats_seances:
            print(f"id: {seance[0]}, date: {seance[1]}, exercices: {seance[2]}")
        self.user_selection = input("Choix de la seance: ")
        # return user_selection

    def listes_exos(self, liste_exo_data):
        for table_exo in liste_exo_data:
            dict_exercices = {}
            self.cur.execute(f"SELECT * FROM {table_exo} WHERE seances_id = {int(self.user_selection)}")

            listes_seance = self.cur.fetchall()
            print("Liste des exos: ", listes_seance)
            # Output: [(3, 5, 10, 20.0)]
            dict_exercices["name"] = self.format_data(table_exo)
            dict_exercices["seances"] = []

            for index, seance in enumerate(listes_seance):
                dict_exercices["seances"].append(f"{seance[1]} séries de {seance[2]} reps à "
                                                                     f"{seance[3]} Kg")
            self.dict_extract["exercices"].append(dict_exercices)

    def process_extract_seance(self):
        with sqlite3.connect(self.database) as self.conn:  # Context manager auto-ferme
            self.cur = self.conn.cursor()
            self.cur.execute("SELECT * FROM seances ORDER BY id")
            resultats_seances = self.cur.fetchall()
            self.menu_choix_seance(resultats_seances)

            self.dict_extract["date"] = str(resultats_seances[int(self.user_selection)-1][1])
            self.dict_extract["exercices"] = []

            # (1, '23/05/2026', 'squats biceps')
            liste_exo_data = list(resultats_seances[int(self.user_selection)-1])[2].split(" ")
            print("Listes des exos1: ", liste_exo_data)
            self.listes_exos(liste_exo_data)

        return self.dict_extract


    def list_all_tables(self):
        """
        NOT USED
        Permet d'afficher toutes les tables présentes sans la table sqlite qui gère l'autoincrémente de la private key
        :return:
        """
        self.connexion()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        tables = self.cur.fetchall()
        print("Tables de la bd: ", tables)
        self.db_save_and_close()

    def format_data(self, nom_table):

        if nom_table.count("_"):
            nom_table = nom_table.replace("_", " ")

        return nom_table.capitalize()

if __name__ == "__main__":
    test = Extract_datas("tests.db").process_extract_seance()
    print("Output:\n", test)