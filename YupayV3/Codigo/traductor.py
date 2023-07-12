"""
Módulo para traducir números enteros en Kichwa
"""
from colorama import init, Fore

# Inicializar colorama
init()


class Traductor:
    """
    Clase para traducir números enteros en Kichwa
    """

    @staticmethod
    def numero_a_kichwa(numero):
        """
        Método para traducir un número en Kichwa
        """
        # Cambio de palabras
        unidades = [
            "illak",
            "shuk",
            "ishkay",
            "kimsa",
            "chusku",
            "pichka",
            "sukta",
            "kanchis",
            "pusak",
            "iskun",
        ]
        modificador_posicion = ["", " chunka", " patsak", " waranka"]

        try:
            if not numero:
                print(Fore.RED + "No se ha proporcionado ningún valor de entrada")
                return None

            if isinstance(numero, str):
                numero = numero.replace(',', '.')

            numero_float = float(numero)  # Verificación de tipo de dato
            if not numero_float.is_integer():
                print("El número decimal se trunca")
            numero_int = int(numero_float)
            if numero_int == 0:
                return unidades[0]
            if numero_int < 1 or numero_int > 9999:
                print(Fore.RED + "Debe ingresar un número entre 0 y 9999")
                return None

            numero_str = str(numero_int)
            longitud = len(numero_str)
            resultado = ""

            # Asignación de resultado
            for i in range(longitud):
                if int(numero_str[i]) != 0:
                    # Añade una separación si no es el primer número
                    if i != 0:
                        resultado += " "
                    if (
                        int(numero_str[i]) == 1 and i != longitud - 1
                    ):  # Controlar 1, 10, 100 y 1000
                        resultado += (
                            modificador_posicion[longitud - 1 - i][1:]
                        )
                        continue
                    resultado += (
                        unidades[int(numero_str[i])]
                        + modificador_posicion[longitud - 1 - i]
                    )

            return resultado

        except ValueError:
            print(Fore.RED + "El valor ingresado no es un número entero.")
            return None

    @staticmethod
    def traducir_numero(numero):
        """
        Método para traducir un número en Kichwa (adaptación de nombre)
        """
        return Traductor.numero_a_kichwa(numero)
