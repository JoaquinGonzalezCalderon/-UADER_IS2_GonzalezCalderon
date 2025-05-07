class Pieza:
    def mostrar(self):
        pass

class PiezaConcreta(Pieza):
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def mostrar(self):
        print(f"Pieza: {self.nombre}")

class Subconjunto(Pieza):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.piezas = []
    
    def agregar(self, pieza: Pieza):
        self.piezas.append(pieza)
    
    def mostrar(self):
        print(f"Subconjunto: {self.nombre}")
        for pieza in self.piezas:
            pieza.mostrar()

# Crear el ensamblado principal
ensamblado = Subconjunto("Producto Principal")
subconjunto1 = Subconjunto("Subconjunto 1")
subconjunto2 = Subconjunto("Subconjunto 2")
subconjunto3 = Subconjunto("Subconjunto 3")

# Agregar piezas a los subconjuntos
subconjunto1.agregar(PiezaConcreta("Pieza 1"))
subconjunto1.agregar(PiezaConcreta("Pieza 2"))
subconjunto1.agregar(PiezaConcreta("Pieza 3"))
subconjunto1.agregar(PiezaConcreta("Pieza 4"))

subconjunto2.agregar(PiezaConcreta("Pieza 5"))
subconjunto2.agregar(PiezaConcreta("Pieza 6"))
subconjunto2.agregar(PiezaConcreta("Pieza 7"))
subconjunto2.agregar(PiezaConcreta("Pieza 8"))

subconjunto3.agregar(PiezaConcreta("Pieza 9"))
subconjunto3.agregar(PiezaConcreta("Pieza 10"))
subconjunto3.agregar(PiezaConcreta("Pieza 11"))
subconjunto3.agregar(PiezaConcreta("Pieza 12"))

# Agregar subconjuntos al ensamblado
ensamblado.agregar(subconjunto1)
ensamblado.agregar(subconjunto2)
ensamblado.agregar(subconjunto3)

# Mostrar la estructura
ensamblado.mostrar()
