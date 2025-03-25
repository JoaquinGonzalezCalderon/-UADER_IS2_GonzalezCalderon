#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

import sys

def factorial(num): 
    if num < 0: 
        print(f"Factorial de {num} no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) != 2:
    print("Debe informar un rango de números en los formatos: desde-hasta, -hasta o desde-")
    sys.exit()

arg = sys.argv[1]

try:
    if '-' in arg:
        if arg.startswith('-'):  # Caso "-hasta"
            hasta = int(arg[1:])  # Convertir la parte numérica a entero
            desde = 1
        elif arg.endswith('-'):  # Caso "desde-"
            desde = int(arg[:-1])  # Convertir la parte numérica a entero
            hasta = 60
        else:  # Caso "desde-hasta"
            desde, hasta = map(int, arg.split('-'))

        if desde > hasta:
            print("El primer número debe ser menor o igual al segundo.")
            sys.exit()

        for num in range(desde, hasta + 1):
            print(f"Factorial {num}! es {factorial(num)}")

    else:
        print("Formato incorrecto. Debe ingresar un rango válido como -10, 5-20 o 15-")
except ValueError:
    print("Error: Asegúrese de ingresar valores numéricos correctamente.")



