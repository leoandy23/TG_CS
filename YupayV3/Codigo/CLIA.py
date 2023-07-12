"""
Módulo CLI
"""
from colorama import init, Fore
from traductor import Traductor

# Inicializar colorama
init()

print("Bienvenido al traductor de números a kichwa.")
FLAG = "S"
while FLAG == "S":
    print(Fore.RESET + "--------------------------------------------------")
    numero = input(Fore.RESET + "Ingresa un número entre 0 y 9999: ")
    texto_kichwa = Traductor.numero_a_kichwa(numero)
    if texto_kichwa is not None:
        print(Fore.GREEN + "El número en kichwa es:", texto_kichwa)

    FLAG = input(Fore.RESET + "Ingrese \"S\" para volver a usar el traductor: ").upper()

print(Fore.RESET + "--------------------------------------------------")
print(Fore.RESET + "Gracias por usar el traductor de números a kichwa.")
