import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------

"""State class: Base State class"""
class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.all_stations):
            self.pos = 0
        freq, label = self.all_stations[self.pos]
        if label.startswith("M"):
            print("Sintonizando... Memoria {} {} ({})".format(label, freq, self.name))
        else:
            print("Sintonizando... Estación {} {}".format(freq, self.name))

#*------- Implementa cómo barrer las estaciones de AM
class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = [("1250", "E1"), ("1380", "E2"), ("1510", "E3")]
        self.name = "AM"
        self.update_all_stations()

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def update_all_stations(self):
        self.all_stations = self.stations + [
            (freq, mem) for mem, (band, freq) in self.radio.memories.items() if band == "AM"
        ]
        self.pos = -1

#*------- Implementa cómo barrer las estaciones de FM
class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = [("81.3", "E1"), ("89.1", "E2"), ("103.9", "E3")]
        self.name = "FM"
        self.update_all_stations()

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def update_all_stations(self):
        self.all_stations = self.stations + [
            (freq, mem) for mem, (band, freq) in self.radio.memories.items() if band == "FM"
        ]
        self.pos = -1

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:
    def __init__(self):
        # Memorias M1 a M4, pueden ser AM o FM
        self.memories = {
            "M1": ("AM", "1250"),
            "M2": ("FM", "103.9"),
            "M3": ("FM", "89.1"),
            "M4": ("AM", "1380"),
        }

        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        # Inicialmente en FM
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()
        self.update_memories()

    def scan(self):
        self.state.scan()

    def update_memories(self):
        self.amstate.update_all_stations()
        self.fmstate.update_all_stations()

#*---------------------
# Ejemplo de uso
if __name__ == "__main__":
    radio = Radio()
    for _ in range(10):
        radio.scan()

    radio.toggle_amfm()
    for _ in range(10):
        radio.scan()
