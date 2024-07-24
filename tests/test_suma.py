import unittest

from proyecto.suma import sumar

class TestSuma(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2,3),5)
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(-3,-2),-5)
        
if __name__ == '__main__':
    unittest.main()