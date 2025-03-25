#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
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
   print("Debe informar un rango de números en el formato desde-hasta (ej. 4-8)!")
   sys.exit()

try:
    # Separar los valores del rango
    desde, hasta = map(int, sys.argv[1].split('-'))
    
    if desde > hasta:
        print("El primer número debe ser menor o igual al segundo.")
        sys.exit()
    
    for num in range(desde, hasta + 1):
        print(f"Factorial {num}! es {factorial(num)}")

except ValueError:
    print("Formato incorrecto. Debe ingresar dos números separados por un guion (ej. 4-8).")


