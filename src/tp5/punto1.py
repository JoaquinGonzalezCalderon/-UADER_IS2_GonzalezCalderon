class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, number):
        if self.next_handler:
            return self.next_handler.handle(number)
        else:
            print(f"{number} no fue consumido.")
            return None

class PrimeHandler(Handler):
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} fue consumido por PrimeHandler")
        else:
            super().handle(number)

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} fue consumido por EvenHandler")
        else:
            super().handle(number)

# Crear la cadena
prime_handler = PrimeHandler()
even_handler = EvenHandler()

prime_handler.set_next(even_handler)

# Probar con números del 1 al 100
for i in range(1, 101):
    prime_handler.handle(i)
