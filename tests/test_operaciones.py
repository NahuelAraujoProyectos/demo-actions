import unittest

from proyecto.operaciones import sumar, resta

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2,3),5)
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(-3,-2),-5)
    
    def test_resta(self):
        self.assertEqual(resta(2,3),-1)
        self.assertEqual(resta(5,2),3)
        self.assertEqual(resta(4,4),0)
    
if __name__ == '__main__':
    unittest.main()