from Traductor import Traductor
from colorama import init, Fore

# Inicializar colorama
init()

print("Bienvenido al traductor de números a kichwa.")
flag = "S"
while flag == "S":
    print(Fore.RESET + "--------------------------------------------------")
    numero = input(Fore.RESET + "Ingresa un número entre 0 y 9999: ")
    texto_kichwa = Traductor.numero_a_kichwa(numero)
    if (
        texto_kichwa is not None
    ):  # Evitar la impresión en caso de que no exista un retorno.
        print(Fore.GREEN + "El número en kichwa es:", texto_kichwa)

    flag = input(Fore.RESET + "Ingrese \"S\" para volver a usar el traductor: ").upper()

print(Fore.RESET + "--------------------------------------------------")
print(Fore.RESET + "Gracias por usar el traductor de números a kichwa.")
