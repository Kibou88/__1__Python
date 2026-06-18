"""
Ecriture du rapport
---------------------------
But:
Mettre en forme les informations de l'extraction et sauvegarder sous un txt
"""
from extract_datas import Extract_datas

class Write_report:

    def __init__(self, filename: str, database: str):
        self.filename = filename

        if database.endswith('.db'):
            self.database = database
            self.dict_extract = {}
        else:
            self.database = database + ".db"

        self.report_contents = []

    def create_txt_file(self):
        try:
            with open(self.filename, "x", encoding="utf-8") as file:
                for line in self.report_contents:
                    file.write(line)

        except FileExistsError:
            print("Fichier deja existant")

    def dict_extract_datas(self):
        self.dict_extracted = Extract_datas("tests.db").list_items_table_seances()

    def type_separator(self, type_sep):
        if type_sep == 1:
            self.report_contents.append("\n==============================")
        elif type_sep == 2:
            self.report_contents.append(f"\n-----------------------------")

    def report_title(self):
        self.report_contents.append(f"\tRapport du {self.dict_extracted["date"]}")

    def report_exercices(self, j):
        self.report_contents.append(f"\n- Exercice: {self.dict_extracted['exercices'][j]['name']}")

    def report_seances(self, i, j):
        self.report_contents.append(f"\n\t* {self.dict_extracted['exercices'][j]['seances'][i]}")

    def process_write_report(self):
        self.dict_extracted = Extract_datas(self.database).list_items_table_seances()
        self.report_title()
        self.type_separator(1)
        for j in range(len(self.dict_extracted["exercices"])):
            self.report_exercices(j)
            for i in range(len(self.dict_extracted['exercices'][j]['seances'])):
                self.report_seances(i, j)
            self.type_separator(2)
        # self.type_separator(1)
        print(self.report_contents)

        self.create_txt_file()

if __name__ == "__main__":
    # test = Extract_datas("tests.db").list_items_table_seances()
    # print(len(test['exercices']))
    Write_report("write_report.txt", "tests.db").process_write_report()