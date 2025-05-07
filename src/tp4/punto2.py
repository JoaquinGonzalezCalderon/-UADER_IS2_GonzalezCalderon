class TrenLaminador:
    def laminar(self, espesor: float, ancho: float):
        pass

class TrenLaminador5m(TrenLaminador):
    def laminar(self, espesor: float, ancho: float):
        print(f"Laminando una lámina de {espesor} de espesor y {ancho} de ancho con tren de 5m.")

class TrenLaminador10m(TrenLaminador):
    def laminar(self, espesor: float, ancho: float):
        print(f"Laminando una lámina de {espesor} de espesor y {ancho} de ancho con tren de 10m.")

class LaminaAcero:
    def __init__(self, espesor: float, ancho: float, tren: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren
    
    def producir(self):
        self.tren.laminar(self.espesor, self.ancho)

# Creamos trenes laminadores
tren_5m = TrenLaminador5m()
tren_10m = TrenLaminador10m()

# Creamos láminas con distintos trenes laminadores
lamina1 = LaminaAcero(0.5, 1.5, tren_5m)
lamina1.producir()

lamina2 = LaminaAcero(0.5, 1.5, tren_10m)
lamina2.producir()
