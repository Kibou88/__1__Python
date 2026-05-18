# setUp/tearDown
# - Apprendre à utiliser setUp/tearDown
##############################################
"""
setUp : pour préparer l’état nécessaire à vos tests (exemple : instancier objets, ouvrir fichiers, connecter bases…)

tearDown : pour nettoyer ou réinitialiser après chaque test (exemple : fermer fichiers/connexions, supprimer
ressources temporaires)

Ces méthodes sont appelées avant et après chaque méthode de test, garantissant ainsi que chaque test commence avec un
environnement propre et cohérent.
"""
import unittest

def multiplication(a, b):
    return a * b

class TestOperations(unittest.TestCase):

    def setUp(self):
        # Cette méthode est appelée **avant chaque test**
        # Elle sert à initialiser les variables ou préparer l’environnement
        print("Préparation du test")
        self.x = 2
        self.y = 3

    def tearDown(self):
        # Cette méthode est appelée **après chaque test**
        # Elle sert à nettoyer ou réinitialiser l’environnement
        # (exemple : fermer fichiers / connexions, supprimer ressources temporaires)
        print("Nettoyage après le test")

    def test_addition(self):
        # Exemple : test d'une addition simple
        result = self.x + self.y
        self.assertEqual(result, 5)

    def test_multiplication(self):
        # Test de la fonction multiplication avec les variables préparées
        result = multiplication(self.x, self.y)
        self.assertEqual(multiplication(self.x, self.y), 6)

if __name__ == '__main__':
    unittest.main()