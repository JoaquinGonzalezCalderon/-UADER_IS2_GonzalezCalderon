import os

#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo mejorado
#*--------------------------------------------------------------------
class Memento:
	def __init__(self, file, content):
		self.file = file
		self.content = content


class FileWriterUtility:
	def __init__(self, file):
		self.file = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	def __init__(self):
		self.history = []

	def save(self, writer):
		if len(self.history) == 4:
			self.history.pop(0)  # Elimina el más antiguo si hay 4
		self.history.append(writer.save())

	def undo(self, writer, index=0):
		if 0 <= index < len(self.history):
			writer.undo(self.history[-(index + 1)])
		else:
			print(f"No hay estado guardado en la posición {index}.")


if __name__ == '__main__':
	os.system("clear")
	print("Crea un objeto que gestionará las versiones anteriores")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	print("Se graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional II")
	writer.write("Material adicional II\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional III")
	writer.write("Material adicional III\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	print("Se graba información adicional IV (ya hay 4 guardadas)")
	writer.write("Material adicional IV\n")
	print(writer.content + "\n")
	caretaker.save(writer)

	# Pruebas de undo
	print("Undo(0) → Revierte al estado anterior inmediato")
	caretaker.undo(writer, 0)
	print(writer.content + "\n")

	print("Undo(2) → Revierte al tercer estado hacia atrás")
	caretaker.undo(writer, 2)
	print(writer.content + "\n")

	print("Undo(3) → Revierte al cuarto estado hacia atrás (el más antiguo disponible)")
	caretaker.undo(writer, 3)
	print(writer.content + "\n")

	print("Undo(4) → No existe (fuera de rango)")
	caretaker.undo(writer, 4)
