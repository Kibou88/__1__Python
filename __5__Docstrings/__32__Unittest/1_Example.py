# Unittest
# - Apprendre à utiliser la librairie unittest
##############################################
"""
Structure de base:
On crée une classe de test héritant de unittest.TestCase. Chaque test est une méthode de cette classe
dont le nom commence par test_.

Méthodes AAA:
Chaque test suit trois étapes clés (AAA) :
- Arrange : mettre en place les conditions du test (variables, objets à tester)
- Act : exécuter la fonction ou la méthode à tester
- Assert : vérifier le résultat attendu avec des méthodes d’assertion (ex. assertEqual, assertTrue, etc.)
"""
import unittest

def add(a, b):
    return a + b

def multiplication(a, b):
    return a * b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        # assertEqual: La fonction prends 1 et 2 en param et doit renvoyer 3
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -1)

    def test_add_multiple_positive_numbers(self):
        self.assertEqual(multiplication(1, 2), 2)
if __name__ == '__main__':
    unittest.main()