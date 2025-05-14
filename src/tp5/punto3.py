class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def emit_id(self, id_value):
        print(f"\nEmitiendo ID: {id_value}")
        for obs in self.observers:
            obs.notify(id_value)

class Observer:
    def __init__(self, my_id):
        self.my_id = my_id

    def notify(self, id_value):
        if id_value == self.my_id:
            print(f"Observer {self.my_id} recibió su ID.")

# Crear el sujeto
subject = Subject()

# Crear observadores con IDs específicos
obs1 = Observer("AB12")
obs2 = Observer("XY34")
obs3 = Observer("ZZ99")
obs4 = Observer("QWER")

# Subscribir observadores al sujeto
subject.subscribe(obs1)
subject.subscribe(obs2)
subject.subscribe(obs3)
subject.subscribe(obs4)

# Emitir 8 IDs (al menos 4 deben coincidir con los observers)
ids_a_emitir = ["AB12", "1234", "XY34", "TEST", "ZZ99", "QWER", "AAAA", "BBBB"]

for id_emitted in ids_a_emitir:
    subject.emit_id(id_emitted)
