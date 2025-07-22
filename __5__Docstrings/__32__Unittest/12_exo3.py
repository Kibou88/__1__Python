"""
Écrire une fonction factorielle(n)

Calcule la factorielle d’un entier positif.

Tester cette fonction avec les valeurs 0, 1, 5 et un nombre négatif (qui doit être géré via une exception
ou un message d’erreur).
"""
import unittest

def factorial(n):
    if n < 0:
        raise ValueError('n doit etre un nombre positif')
    if n == 0:
        return 1
    return n * factorial(n - 1)

class TestFactorial(unittest.TestCase):
    def setUp(self):
        self.zero = 0
        self.one = 1
        self.five = 5
        self.negative = -5

    def test_factorial_zero(self):
        f = factorial(self.zero)
        self.assertEqual(f, 1)

    def test_factorial_one(self):
        f = factorial(self.one)
        self.assertEqual(f, 1)

    def test_factorial_five(self):
        f = factorial(self.five)
        self.assertEqual(f, 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(self.negative)

if __name__ == '__main__':
    unittest.main()