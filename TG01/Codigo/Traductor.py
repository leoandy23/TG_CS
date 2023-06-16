class Traductor():

    # return número en kichwa entre 0 y 9,999
    @staticmethod
    def numero_a_kichwa(numero):
        # Cambio de palabras
        unidades = ['illak', 'shuk', 'ishkay', 'kimsa', 'chusku', 'pichka', 'sukta', 'kanchis', 'pusak', 'iskun']
        modificadorPosicion = ['',' chunka',' patsak',' waranka']

        try:
            numero_float = float(numero) # Verificación de tipo de dato
            if (numero_float.is_integer()==False):
                print("El número decimal se trunca")
            numero_int = int(numero_float) # Conversión a enteros
            if numero_int == 0:
                return unidades[0]
            if numero_int > 0 and numero_int <= 9999: # Verificación de rango
                numero_str = str(numero_int)
                longitud = len(numero_str)
                resultado = ''

                # Asignación de resultado
                for i in range (longitud):
                    if (int(numero_str[i])!=0):
                        if (i!=0): #Añade una separación si no es el primer número
                            resultado += " "
                        if (int(numero_str[i])==1 and i!=longitud-1): #Controlar 1, 10, 100 y 1000
                            resultado += modificadorPosicion[longitud-1-i][1:]
                            continue
                        resultado +=  unidades[int(numero_str[i])] + modificadorPosicion[longitud-1-i]
                return resultado
            else:
                print("Debe ingresar un número entre 0 y 9,999")
        except ValueError:
            print("El valor ingresado no es un número entero.")

