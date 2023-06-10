from Traductor import Traductor

numero = int(input('Ingresa un número entre 0 y 9,999: '))
texto_kichwa = Traductor.numero_a_kichwa(numero)
print('El número en kichwa es:', texto_kichwa)