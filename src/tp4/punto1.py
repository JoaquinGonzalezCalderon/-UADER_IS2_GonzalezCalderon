import os

class Ping:
    def __init__(self, ip: str):
        self.ip = ip

    def execute(self):
        # Solo ejecuta el ping si la IP comienza con "192."
        if self.ip.startswith("192."):
            print(f"Ejecutando ping a {self.ip}")
            for _ in range(10):  # Hacemos 10 intentos de ping
                response = os.system(f"ping -n 1 {self.ip}")
                if response == 0:
                    print(f"Ping a {self.ip} exitoso.")
                else:
                    print(f"Ping a {self.ip} fallido.")
        else:
            print("La dirección IP debe comenzar con '192.' para realizar el ping.")
    
    def executefree(self, ip: str):
        # Método que realiza ping sin control de IP
        print(f"Ejecutando ping libre a {ip}")
        for _ in range(10):  # Hacemos 10 intentos de ping
            response = os.system(f"ping -n 1 {ip}")
            if response == 0:
                print(f"Ping a {ip} exitoso.")
            else:
                print(f"Ping a {ip} fallido.")

class PingProxy:
    def __init__(self, ip: str):
        self.ping = Ping(ip)

    def execute(self, ip: str):
        # Si la IP es "192.168.0.254", hacer ping a Google
        if ip == "192.168.0.254":
            print("Dirección IP especial detectada. Redirigiendo a www.google.com")
            self.ping.executefree("www.google.com")
        else:
            # Si no, hacer ping normal
            self.ping.execute()

# Probamos la clase PingProxy con varias direcciones IP
ping_proxy = PingProxy("192.168.0.1")
ping_proxy.execute("192.168.0.1")  # Debería ejecutar ping normal

print("\n")
ping_proxy.execute("192.168.0.254")  # Debería redirigir a Google
