"""
    Módulo para testear la traducción números enteros en Kichwa
"""

import unittest
from traductor import Traductor


class TestMyModule(unittest.TestCase):
    """
    Clase de pruebas para el módulo Traductor
    """

    def test_numero_kichwa(self):
        """
        Prueba para la función numero_a_kichwa
        """
        resultado = Traductor.numero_a_kichwa(7)
        self.assertEqual(resultado, "kanchis")

        resultado = Traductor.numero_a_kichwa(59)
        self.assertEqual(resultado, "pichka chunka iskun")

        resultado = Traductor.numero_a_kichwa(864)
        self.assertEqual(resultado, "pusak patsak sukta chunka chusku")

        resultado = Traductor.numero_a_kichwa(3201)
        self.assertEqual(resultado, "kimsa waranka ishkay patsak shuk")


if __name__ == "__main__":
    unittest.main()
