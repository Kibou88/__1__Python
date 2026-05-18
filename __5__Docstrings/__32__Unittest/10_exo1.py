"""
Écrire une fonction est_pair(n)

Elle doit retourner True si n est pair, sinon False.

Gérez aussi le cas où l’entrée n’est pas un entier (par exemple une chaîne) en levant une exception ou en retournant une valeur spécifique.

Écrire des tests unitaires pour est_pair(n)
Testez les cas suivants :

Un nombre pair (ex : 2, 0) doit retourner True.

Un nombre impair (ex : 3, 1) doit retourner False.

Une entrée invalide (ex : "test") doit lever une exception ou être gérée correctement.
"""
import unittest

def est_pair(n):
    if not isinstance(n, int):
        raise TypeError("n doit etre un nombre")
    return n % 2 == 0

class Test_est_pair(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = 3
        self.c = "Test"

    def test_est_pair(self):
        self.assertTrue(est_pair(self.a))

    def test_est_impair(self):
        self.assertFalse(est_pair(self.b))

    def test_erreur_type(self):
        with self.assertRaises(TypeError):
            est_pair(self.c)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()