"""
Project: Trier fichiers
---------------------
manage_file.py
But: Contain the class to manage datas from files
--------------------------------
Creation date: 2025-05-12
Modification date: 2025-05-12
--------------------------------
Version: 1.0
"""

from pathlib import Path
import logging
import os
import time

# Initialisation du fichier de log pour la classe
logging.basicConfig(level=logging.INFO,
                        filename="Manage_file.log",
                        filemode="a+",
                        format='%(asctime)s - %(levelname)s - %(message)s')

class Manage_file:

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def creation_time(self):
        return time.localtime(os.path.getctime(self.file_path))

    def modification_time(self):
        return time.localtime(os.path.getmtime(self.file_path))

    def comparaison(self):

        print("file modification: ", self.modification_time().tm_year)
        print("file creation: ", self.creation_time().tm_year)

        if self.creation_time().tm_year > self.modification_time().tm_year:
            year = self.modification_time().tm_year
            print("File modification choisie")
            month = self.modification_time().tm_mon
        else:
            year = self.creation_time().tm_year
            print("File creation choisie")
            month = self.creation_time().tm_mon



if __name__ == "__main__":
    test = \
        "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\" \
        "__12__Trier_fichiers\\venv\\test.jpg"

    test2 = \
        "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\" \
        "__12__Trier_fichiers\\venv\\Log.txt"

    file = Manage_file(test)
    file2 = Manage_file(test2)
    
    file.comparaison()
    file2.comparaison()