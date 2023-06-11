from Traductor import Traductor

numero = input('Ingresa un número entre 0 y 9,999: ')
texto_kichwa = Traductor.numero_a_kichwa(numero)
if (texto_kichwa != None): # Evitar la impresión en caso de que no exista un retorno.
    print('El número en kichwa es:', texto_kichwa)