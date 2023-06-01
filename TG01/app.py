def numero_a_kichwa(numero):
    unidades = ['', 'shuk', 'ishkay', 'kimsa', 'tawa', 'pichka', 'sukta', 'kanchi', 'pichka kimsa', 'pichka tawa']
    decenas = ['', 'chunka', 'ishkay chunka', 'kimsa chunka', 'tawa chunka', 'pichka chunka', 'sukta chunka', 'pichka ishkay chunka', 'pichka kimsa chunka', 'pichka tawa chunka']
    centenas = ['', 'chunka huasi', 'ishkay chunka huasi', 'kimsa chunka huasi', 'tawa chunka huasi', 'pichka chunka huasi', 'sukta chunka huasi', 'pichka ishkay chunka huasi', 'pichka kimsa chunka huasi', 'pichka tawa chunka huasi']
    miles = ['', 'chunka kallari', 'ishkay chunka kallari', 'kimsa chunka kallari', 'tawa chunka kallari', 'pichka chunka kallari', 'sukta chunka kallari', 'pichka ishkay chunka kallari', 'pichka kimsa chunka kallari', 'pichka tawa chunka kallari']

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
