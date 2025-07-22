import unittest

def add_safe(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    return a + b

class TestAddSafe(unittest.TestCase):
    def test_add_valid(self):
        self.assertEqual(add_safe(5, 3), 8)

    def test_add_invalid(self):
        self.assertFalse(add_safe("grg", 3))

if __name__ == '__main__':
    unittest.main()
