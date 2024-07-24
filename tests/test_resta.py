import unittest

from proyecto.resta import resta

class TestResta(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(5,4),1)
        self.assertEqual(resta(2,3),1)
        self.assertEqual(resta(6,6),0)

if __name__ == '__main__':
    unittest.main()