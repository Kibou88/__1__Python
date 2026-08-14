"""
Ajouter les données d'un dico (format identique à celui du projet) dans la base de données
---------------------------
But:
Premier pas avec SQLite3
Création d'une bade de données avec lecture
"""
import json
import sqlite3  # Import standard

from Manage_DataBase import DataBase

class Analyse_dico:

    def __init__(self, dico=None):
        if not type(dico) == dict and dico.endswith(".json"):
            with open(dico, "r") as file:
                self.data = json.load(file)
            print(self.data)
        elif isinstance(dico, dict):
            self.data = dico
            print(self.data)
        else:
            print("Type de dico n'est pas valide")
            exit(1)


    def analyse_dico_user(self):
        compact_datas = []
        liste_exos = []

        self.date_seance = self.data["date"]
        compact_datas.append(self.date_seance)
        self.nombre_exo = len(self.data["exercices"])
        print(self.date_seance)
        print(self.nombre_exo)

        for i in range(self.nombre_exo):
            print(self.data["exercices"][i]["name"]) # Affiche juste le nom
            # print(self.data["exercices"][i]["seance"]) # Affiche toutes les séries de l'exo

            if(self.data["exercices"][i]["name"].count(" ")):
                self.data["exercices"][i]["name"] = self.data["exercices"][i]["name"].replace(" ", "_")
            # liste_exos.append(self.data["exercices"][i]["name"])


            nombre_seance = len(self.data["exercices"][i]["seance"])
            liste_series_reps_load = [self.data["exercices"][i]["name"].lower()]
            for j in range(nombre_seance):
                print(f"Serie {j+1}: series {self.data["exercices"][i]["seance"][j]["series"]}, "
                      f"reps {self.data["exercices"][i]["seance"][j]["reps"]}, "
                      f"charges {self.data["exercices"][i]["seance"][j]["loads"]} Kg")
                liste_series_reps_load.append([self.data["exercices"][i]["seance"][j]["series"],
                                               self.data["exercices"][i]["seance"][j]["reps"],
                                               self.data["exercices"][i]["seance"][j]["loads"]])
            compact_datas.append(liste_series_reps_load)
        # Format: ['28/03/26', ['squats', [10, 20, 30], [20, 30, 40]], ['fentes_avant', [10, 20, 35]]]
        return compact_datas


class Add_datas_DB:

    def __init__(self):
        pass



if __name__ == "__main__":
    # dico = Analyse_dico(test_dict)
    dico = Analyse_dico("test_dico_user.json")
    # compact_datas_ready = dico.analyse_dico_user()
    # for i in len(compact_datas_ready):
    test_datas = [('28/03/26', 'squats fentes_avant')]
    config_colonne = ["id INTEGER PRIMARY KEY AUTOINCREMENT",
            "date TEXT NOT NULL",
            "exercices TEXT NOT NULL"]
    name_colonne = ["date", "exercices", "poids"]
    database_seance = DataBase(dbName="test_db_seance.db", dbTableName="seance")
    database_seance.create_table(config_colonne=config_colonne)
    database_seance.write_datas_table("seance", test_datas, name_colonne)