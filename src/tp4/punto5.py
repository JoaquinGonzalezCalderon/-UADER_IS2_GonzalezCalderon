class Carácter:
    def __init__(self, tipo: str):
        self.tipo = tipo

    def mostrar(self):
        print(f"Mostrando el carácter: {self.tipo}")

class FabricaCaracteres:
    def __init__(self):
        self.caracteres = {}

    def obtener(self, tipo: str):
        if tipo not in self.caracteres:
            self.caracteres[tipo] = Carácter(tipo)
        return self.caracteres[tipo]

# Usar la fábrica para crear objetos compartidos
fabrica = FabricaCaracteres()

caracter_A = fabrica.obtener("A")
caracter_B = fabrica.obtener("B")
caracter_C = fabrica.obtener("A")  # Se reutiliza la "A" existente
