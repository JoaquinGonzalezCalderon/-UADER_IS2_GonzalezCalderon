class Numero:
    def __init__(self, valor: float):
        self.valor = valor

    def mostrar(self):
        print(f"Valor: {self.valor}")

class Operacion(Numero):
    def __init__(self, numero: Numero):
        self.numero = numero

    def mostrar(self):
        self.numero.mostrar()

class Sumar(Operacion):
    def __init__(self, numero: Numero, suma: float):
        super().__init__(numero)
        self.suma = suma

    def mostrar(self):
        self.numero.mostrar()
        print(f"Sumando {self.suma}")
        self.numero.valor += self.suma
        self.numero.mostrar()

class Multiplicar(Operacion):
    def __init__(self, numero: Numero, multiplicador: float):
        super().__init__(numero)
        self.multiplicador = multiplicador

    def mostrar(self):
        self.numero.mostrar()
        print(f"Multiplicando por {self.multiplicador}")
        self.numero.valor *= self.multiplicador
        self.numero.mostrar()

class Dividir(Operacion):
    def __init__(self, numero: Numero, divisor: float):
        super().__init__(numero)
        self.divisor = divisor

    def mostrar(self):
        self.numero.mostrar()
        print(f"Dividiendo por {self.divisor}")
        self.numero.valor /= self.divisor
        self.numero.mostrar()

numero = Numero(10)

# Decoradores
numero = Sumar(numero, 2)
numero = Multiplicar(numero, 2)
numero = Dividir(numero, 3)

numero.mostrar()
