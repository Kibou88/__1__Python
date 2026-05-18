import unittest

def add_safe(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    return a + b

class TestAddSafe(unittest.TestCase):

    def test_assert_equal(self):
        # Vérifie que deux valeurs sont exactement égales
        self.assertEqual(add_safe(5, 3), 8)

    def test_assert_true(self):
        # Vérifie qu'une condition est vraie
        self.assertTrue(add_safe(2, 2) == 4)

    def test_assert_false(self):
        # Vérifie qu'une condition est fausse
        self.assertFalse(add_safe("grg", 3))

    def test_assert_in(self):
        # Vérifie qu'un élément est présent dans un ensemble, une liste ou une chaîne
        message = "Table créée avec succès"
        self.assertIn("créée", message)

    def test_assert_not_in(self):
        # Vérifie qu'un élément n'est pas présent
        message = "Table créée avec succès"
        self.assertNotIn("erreur", message)

    def test_assert_is_none(self):
        # Vérifie qu'une valeur est None
        value = None
        self.assertIsNone(value)

    def test_assert_is_not_none(self):
        # Vérifie qu'une valeur n'est pas None
        value = 5
        self.assertIsNotNone(value)

    def test_assert_is(self):
        # Vérifie que deux variables pointent vers le même objet
        a = b = []
        self.assertIs(a, b)

    def test_assert_is_not(self):
        # Vérifie que deux variables ne pointent pas vers le même objet
        a = []
        b = []
        self.assertIsNot(a, b)

    def test_assert_raises(self):
        # Vérifie qu'une exception est levée
        with self.assertRaises(TypeError):
            add_safe(5, "x")

if __name__ == '__main__':
    unittest.main()