from colorama import init, Fore

# Inicializar colorama
init()


class Traductor:
    # Retorna número en kichwa entre 0 y 9999
    @staticmethod
    def numero_a_kichwa(numero):
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
            if len(numero) != 0:
                numero = numero.replace(',', '.')
                numero_float = float(numero)  # Verificación de tipo de dato
                if not numero_float.is_integer():
                    print("El número decimal se trunca")
                numero_int = int(numero_float)
                if numero_int == 0 :
                    return unidades[0]
                if 0 < numero_int <= 9999:  # Verificación de rango
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
                else:
                    print(Fore.RED + "Debe ingresar un número entre 0 y 9999")
            else:
                print(Fore.RED + "No se ha proporcionado ningún valor de entrada")
        except ValueError:
            print(Fore.RED + "El valor ingresado no es un número entero.")
