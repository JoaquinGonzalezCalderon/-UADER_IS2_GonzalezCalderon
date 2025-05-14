class StringIterator:
    def __init__(self, text):
        self.text = text

    def forward(self):
        for char in self.text:
            yield char

    def reverse(self):
        for char in reversed(self.text):
            yield char

# Ejemplo de uso
cadena = StringIterator("Hola Mundo")

print("Recorrido en sentido directo:")
for c in cadena.forward():
    print(c, end=' ')
print()

print("Recorrido en sentido reverso:")
for c in cadena.reverse():
    print(c, end=' ')
print()
