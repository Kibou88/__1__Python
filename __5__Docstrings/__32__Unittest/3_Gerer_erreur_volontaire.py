import unittest

def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Les deux arguments doivent être des nombres")
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_valid(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            add("grg", 3)
            print("TypeError bien remonte")

        with self.assertRaises(ValueError):
            add("grg", 3)
            print("problème")

if __name__ == '__main__':
    unittest.main()
