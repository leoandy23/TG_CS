def numero_a_kichwa(numero):
    unidades = ['', 'shuk', 'ishkay', 'kimsa', 'chusku', 'pichka', 'shukta', 'kanchis', 'pushak', 'ishkun']
    decenas = ['', 'chunka', 'ishkay chunka', 'kimsa chunka', 'chusku chunka', 'pichka chunka', 'sukta chunka', 'kanchis chunka', 'pusak chunka', 'iskun chunka']
    centenas = ['', 'patsak', 'ishkay patsak', 'kimsa patsak', 'chusku patsak', 'pichka patsak', 'sukta patsak', 'kanchis patsak', 'pusak patsak', 'iskun patsak']
    miles = ['', 'waranka', 'ishkay waranka', 'kimsa waranka', 'chusku waranka', 'pichka waranka', 'sukta waranka', 'kanchis waranka', 'pusak waranka', 'iskun waranka']

    if numero == 0:
        return 'shuk'
    else:
        numero_str = str(numero)
        longitud = len(numero_str)
        resultado = ''

        if longitud == 1:
            resultado = unidades[numero]
        elif longitud == 2:
            resultado = decenas[int(numero_str[0])] + ' ' + unidades[int(numero_str[1])]
        elif longitud == 3:
            resultado = centenas[int(numero_str[0])] + ' ' + decenas[int(numero_str[1])] + ' ' + unidades[int(numero_str[2])]
        elif longitud == 4:
            resultado = miles[int(numero_str[0])] + ' ' + centenas[int(numero_str[1])] + ' ' + decenas[int(numero_str[2])] + ' ' + unidades[int(numero_str[3])]

        return resultado

# Ejemplo de uso
numero = int(input('Ingresa un número entre 0 y 9,999: '))
texto_kichwa = numero_a_kichwa(numero)
print('El número en kichwa es:', texto_kichwa)
