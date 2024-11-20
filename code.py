import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(3, 2), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_fail_case_one(self):
        self.assertEqual(add(2, 2), 5)  # Intentional fail

    def test_fail_case_two(self):
        self.assertEqual(add(-1, 1), 0)  # Intentional fail

if __name__ == "__main__":
    unittest.main()
