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
    """
    A class to manage file informations and use them

    This class has these methods:
        - creation_time: Retrieve the creation time of the file
        - modification_time: Retrieve the modifiation time of the file
        - comparaison: Return year and month values from the oldest 
    """

    def __init__(self, file_path: Path):
        """
        :param file_path: Path
            Absolute path including file + extension
        """
        self.file_path = file_path

    def creation_time(self):
        """
        Retrieve the creation time of the file specified by `self.file_path`

        :return: struct_time:
            A time object representing the local creation time of the file.
            The object contains attributes such as year, month, day, hour, minute, etc.
        """
        return time.localtime(os.path.getctime(self.file_path))

    def modification_time(self):
        """
        Retrieve the modification time of the file specified by `self.file_path`

        :return: struct_time:
            A time object representing the local modification time of the file.
            The object contains attributes such as year, month, day, hour, minute, etc.
        """
        return time.localtime(os.path.getmtime(self.file_path))

    def comparaison(self):
        """
        Return the year and month time of the file from the oldest value
        i.e:
            - Creation time: year = 2025 / month = 12
            - Modification time: year = 2024 / month = 02
            ==> Return year and month from Modification time
        :return: year, month: int
            Return year and month values
        """
        if self.creation_time().tm_year > self.modification_time().tm_year:
            return self.modification_time().tm_year, self.modification_time().tm_mon
        else:
            return self.creation_time().tm_year, self.creation_time().tm_mon



if __name__ == "__main__":
    test = \
        "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\" \
        "__12__Trier_fichiers\\venv\\test.jpg"

    test2 = \
        "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\" \
        "__12__Trier_fichiers\\venv\\Log.txt"

    file = Manage_file(test)
    file2 = Manage_file(test2)
    
    year, month = file.comparaison()
    year2, month2 = file2.comparaison()
    print(year, month)
    print(year2, month2)
    print(file2.comparaison()[0]) # Revient à récupérer la variable year