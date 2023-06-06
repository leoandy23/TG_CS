import unittest
from app import numero_a_kichwa

class TestMyModule(unittest.TestCase):

    def test_numero_kichwa(self):
        resultado = numero_a_kichwa(7)
        self.assertEqual(resultado,'kanchis')

        resultado = numero_a_kichwa(59)
        self.assertEqual(resultado, 'pichka chunka ishkun')
        
        resultado = numero_a_kichwa(864)
        self.assertEqual(resultado, 'pusak patsak sukta chunka chusku')

        resultado = numero_a_kichwa(3201)
        self.assertEqual(resultado, 'kimsa waranka ishkay patsak  shuk')

if __name__ == '__main__':
    unittest.main()
