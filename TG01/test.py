import unittest
from Traductor import Traductor

class TestMyModule(unittest.TestCase):

    def test_numero_kichwa(self):
        
        resultado = Traductor.numero_a_kichwa(7)
        self.assertEqual(resultado,'kanchis')

        resultado = Traductor.numero_a_kichwa(59)
        self.assertEqual(resultado, 'pichka chunka iskun')
        
        resultado = Traductor.numero_a_kichwa(864)
        self.assertEqual(resultado, 'pusak patsak sukta chunka chusku')

        resultado = Traductor.numero_a_kichwa(3201)
        self.assertEqual(resultado, 'kimsa waranka ishkay patsak shuk')
        
if __name__ == '__main__':
    unittest.main()
