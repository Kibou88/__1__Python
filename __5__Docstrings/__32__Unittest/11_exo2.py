"""
Créer une classe Compteur avec une méthode incrementer()

La méthode doit augmenter une variable interne compteur de 1 à chaque appel.

Écrire des tests qui vérifient que compteur est bien incrémenté même après plusieurs appels.
"""
import unittest

class Compteur:
    def __init__(self, nb_loop):
        if not isinstance(nb_loop, int):
            raise TypeError("nb_loop doit etre un nombre int")
        elif nb_loop <= 0:
            raise ValueError("nb_loop doit etre un nombre positif positif")
        self.nb_loop = nb_loop


    def incrementer(self):
        counter = 0
        for i in range(self.nb_loop):
            counter += 1
        return counter


class TestCompteur(unittest.TestCase):
    def setUp(self):
        self.a = 4
        self.b = -5
        self.c = "Test"

    def test_correct_value(self):
        self.assertEqual(Compteur(self.a).incrementer(), 4)

    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            Compteur(self.b)

    def test_text(self):
        with self.assertRaises(TypeError):
            Compteur(self.c)

if __name__ == '__main__':
    unittest.main()