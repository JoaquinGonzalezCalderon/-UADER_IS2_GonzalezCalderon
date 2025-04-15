#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys  # Importamos sys para manejar argumentos desde la línea de comandos

class Factorial:
    """Clase para calcular factoriales en un rango dado."""

    def __init__(self):
        """Constructor vacío, ya que no necesitamos atributos iniciales."""
        pass

    def calcular(self, num):
        """Método para calcular el factorial de un número de forma iterativa."""
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

    def run(self, min, max):
        """Calcula los factoriales desde 'min' hasta 'max' e imprime los resultados."""
        if min > max:
            print("El primer número debe ser menor o igual al segundo.")
            return
        for num in range(min, max + 1):
            print(f"Factorial {num}! es {self.calcular(num)}")

# Verificamos que el usuario haya ingresado un argumento
if len(sys.argv) != 2:
    print("Debe informar un rango en los formatos: desde-hasta, -hasta o desde-")
    sys.exit()

arg = sys.argv[1]  # Capturamos el argumento ingresado

try:
    # Evaluamos los diferentes formatos de entrada
    if '-' in arg:
        if arg.startswith('-'):  # Caso "-hasta" → Calcula desde 1 hasta "hasta"
            hasta = int(arg[1:])
            desde = 1
        elif arg.endswith('-'):  # Caso "desde-" → Calcula desde "desde" hasta 60
            desde = int(arg[:-1])
            hasta = 60
        else:  # Caso "desde-hasta" → Calcula en un rango definido
            desde, hasta = map(int, arg.split('-'))

        # Crear un objeto de la clase Factorial y ejecutar el cálculo
        fact_calc = Factorial()
        fact_calc.run(desde, hasta)
    else:
        print("Formato incorrecto. Debe ingresar un rango válido como -10, 5-20 o 15-")
except ValueError:
    print("Error: Asegúrese de ingresar valores numéricos correctamente.")





