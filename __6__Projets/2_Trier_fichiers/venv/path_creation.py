"""
Projet: Trier fichiers
---------------------
path_creation.py
But: Contient la classe permettant de créer toutes les variables de path
--------------------------------
Date de création: 2025-05-11
Date de modification: 2025-05-12
--------------------------------
Version: 1.1
- Suppression de contrôle dans la méthode file_path (contrôle fait avant) (V1.1)
- Ajout log dans la méhode path_year_month lors de la création des répertoires (V1.1)
"""

from pathlib import Path
import logging

# Initialisation du fichier de log pour la classe
logging.basicConfig(level=logging.INFO,
                        filename="Path_Creation.log",
                        filemode="a+",
                        format='%(asctime)s - %(levelname)s - %(message)s')


class Path_Creation:
    """
    A class to manage file and folder paths.

    This class provides methods to create and manage file paths and directory paths,
    including the creation of directories based on year and month.
    """


    def __init__(self, user_path: str, dico_month: dict = None):
        """
        :param user_path: str
            The Path object representing the user's working directory.

        :param dico_month: dict, optional
            The dictionary used for converting month numbers to month names.
            For example, { '01': '01_January', '02': '02_February', ... }.
            If not provided, months will be represented by their numerical values.
        """
        self.user_path = Path(user_path)
        self.dico_month = dico_month
        self.logger = logging.getLogger("Path_Creation")

    def file_path(self, file: str) -> Path:
        """
        Create the path including the file to manage
        :param file: str
            Name of the file with this extension
        :return: self.file_path: Path
            The absolute path including the file to manage
        """
        return self.user_path.joinpath(file)

    def path_year_month(self, year: int, month: int) -> Path:
        """
        Create the path and folders (if needing) with this architecture (without dico_month conversion):
        user_path/
            ├── year1/
            │   ├── 01/
            │   ├── 02/
            │   ├── ...
            │   └── 12/
            ├── year2/
            │   ├── 01/
            │   ├── 02/
            │   ├── ...
            │   └── 12/
        :param year: int
            Variable corresponding to the year of creation of the file
        :param month: int
            Variable corresponding to the year of creation of the file
        :return: Path
            The absolute path including year and month
        """
        if self.dico_month != None:
            self.path_year_month = self.user_path.joinpath(str(year), self.dico_month.get(str(month)))
        else:
            self.path_year_month = self.user_path.joinpath(str(year),str(month))

        if not self.path_year_month.exists():
            self.path_year_month.mkdir(exist_ok=True, parents=True)
            self.logger.info(f'Les repertoires {year} et {self.dico_month.get(str(month))} ont ete crees')
        return self.path_year_month


if __name__ == "__main__":
    from constantes.constantes import DICO_MOIS

    user_path = \
        "C:\\Users\\Satoshi\\Desktop\\Code\\__1__Entrainement_Python\\__5__Docstrings\\__90__Projets\\__12__Trier_fichiers\\venv"
    file = "test.jpg"
    year = 2025
    month = 12

    print(Path_Creation(user_path).file_path(file))
    print(Path_Creation(user_path, DICO_MOIS).path_year_month(2025, 12))

    # Test gestion d'erreur si oubie d'extension
    file2 = "test"
    try:
        Path_Creation(user_path).file_path(file2)
    except TypeError as e:
        print(e)
    print("Continuons")