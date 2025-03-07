# lib.py
# - Gestion des classes
# - Permettre à l'utilisateur d'ajouter/supprimer/afficher/vider une liste de course
# - Sauvegarder la liste des courses dans un JSON
###############################################################################################################
import json
from pathlib import Path
class Liste:
    """Classe Liste
    """

    def __init__(self, nom):
        """
        Constructeur init
        :param nom: nom de l'aliment ou de la tâches
        """
        self.nom=nom
        self.liste_produits=[] #Init de la liste pour l'instance de la classe

    def ajouter(self, produit):
        if isinstance(produit, str): #Vérification si 'produit' est bien une chaine de caractère
            if not produit in self.liste_produits:
                print(f"{produit} ajouté")
                self.liste_produits.append(produit)
            else:
                print(f"Le produit {produit} est déjà présent dans la liste")
        else:
            print(f"Le produit {produit} n'est pas valide")

    def supprimer(self, produit):
        if isinstance(produit, str):  # Vérification si 'produit' est bien une chaine de caractère
            print(f"{produit} retiré")
            self.liste_produits.remove(produit)
        else:
            print(f"Le {produit} n'est pas valide")

    def afficher(self):
        print(f'Ma liste de {self.nom}:')
        for produit in self.liste_produits:
            print(f" - {produit}")


    def sauvegarder(self):
        nom_fichier=f"Liste_{self.nom}.json"
        folder_data=Path.cwd() / "data" #Chemin du fichier en partant du répertoire où est lancé l'API
        folder_data.mkdir(exist_ok=True, parents=True) #Créer le dossier "data", si il existe déjà ne retourne pas d'erreur
        fichier_course = folder_data / nom_fichier
        no_exist=False

        try:
            with open(fichier_course, 'r') as file_json:
                read_course=json.load(file_json)
            file_json.close()
        except FileNotFoundError as e:
            print(f"Aucun fichier {nom_fichier} n'existe dans ce répertoire!!")
            no_exist=True

        finally:
            if no_exist:
                print(f"Le fichier {nom_fichier} va être créée")
            else:
                for produit in self.liste_produits:
                    if not produit in read_course:
                        self.liste_produits.append(produit)

            with open(fichier_course, 'w') as file_json:  # Ecriture dans le fichier JSON
                json.dump(self.liste_produits, file_json, indent=4, ensure_ascii=False)
                print(f"Liste des {self.nom} a été sauvegarder")
            file_json.close()

if __name__ == "__main__":
    liste_course = Liste("courses")
    liste_course.ajouter("Pommes")
    liste_course.ajouter("Abricots")
    liste_course.ajouter("Pommes")
    liste_course.sauvegarder()

    liste_taches = Liste("taches")
    liste_taches.ajouter("Finir le travail")
    liste_taches.ajouter("Process")
    liste_taches.sauvegarder()