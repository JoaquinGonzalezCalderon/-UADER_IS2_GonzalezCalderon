#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys  # Importamos el módulo sys para manejar argumentos de línea de comandos

def factorial(num): 
    """Calcula el factorial de un número de forma iterativa."""
    if num < 0: 
        print(f"Factorial de {num} no existe")  # El factorial de números negativos no está definido
        return 0
    elif num == 0: 
        return 1  # Por definición, 0! = 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verificamos que el usuario haya ingresado un argumento
if len(sys.argv) != 2:
    print("Debe informar un rango de números en los formatos: desde-hasta, -hasta o desde-")
    sys.exit()

arg = sys.argv[1]  # Capturamos el argumento ingresado

try:
    # Evaluamos los diferentes formatos de entrada
    if '-' in arg:
        if arg.startswith('-'):  # Caso "-hasta" → Calcula desde 1 hasta "hasta"
            hasta = int(arg[1:])  # Extrae el número después del guion y lo convierte en entero
            desde = 1
        elif arg.endswith('-'):  # Caso "desde-" → Calcula desde "desde" hasta 60
            desde = int(arg[:-1])  # Extrae el número antes del guion y lo convierte en entero
            hasta = 60
        else:  # Caso "desde-hasta" → Calcula en un rango definido
            desde, hasta = map(int, arg.split('-'))  # Separa los números y los convierte en enteros

        # Validamos que el rango sea correcto
        if desde > hasta:
            print("El primer número debe ser menor o igual al segundo.")
            sys.exit()

        # Calculamos y mostramos los factoriales en el rango
        for num in range(desde, hasta + 1):
            print(f"Factorial {num}! es {factorial(num)}")

    else:
        print("Formato incorrecto. Debe ingresar un rango válido como -10, 5-20 o 15-")
except ValueError:
    print("Error: Asegúrese de ingresar valores numéricos correctamente.")




