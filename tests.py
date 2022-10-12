import unittest
from lista_computacion import *
class TestOrdenarResultado(unittest.TestCase):
    def  test_1(self) :
      resultado=OrdenarResultado([5,6,2,1,8])
      self.assertEqual(resultado,[1,2,5,6,8])
    def  test_2(self) :
      resul=OrdenarResultado([7,6,3,2,8])
      self.assertEqual(resul,[2,3,6,7,8])
    def  test_3(self) :
      r=OrdenarResultado([5,2,2,1,8])
      self.assertEqual(r,[1,2,2,5,8])
if __name__ == '__main__':
    unittest.main()