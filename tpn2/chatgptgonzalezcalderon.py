"""
Este módulo permite interactuar con un modelo LLaMA a través de la API local de Ollama.
El usuario puede ingresar consultas que serán enviadas al modelo y recibir una respuesta.
"""

import sys
import requests  # Librería externa para realizar solicitudes HTTP

# Historial para recordar la última consulta
historial = []

def obtener_consulta():
    """Solicita una consulta al usuario y valida que no esté vacía."""
    try:
        consulta = input("Escribí tu consulta para chatGPT (LLaMA): ").strip()
        if not consulta:
            print("La consulta está vacía. Por favor, ingresá un texto.")
            return None
        return consulta
    except KeyboardInterrupt:
        print("\nConsulta cancelada por el usuario.")
        sys.exit()
    except Exception as e:
        print(f"Error al ingresar la consulta: {e}")
        return None

def enviar_consulta(consulta):
    """Envía la consulta al modelo y muestra la respuesta."""
    try:
        print("You:", consulta)
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": consulta,
                "stream": False
            }
        )

        if response.status_code == 200:
            respuesta = response.json().get("response", "Respuesta vacía.")
            print("chatGPT:", respuesta)
        else:
            print("Error al conectar con Ollama:", response.text)

    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con el servidor Ollama. ¿Está corriendo?")
    except requests.exceptions.RequestException as e:
        print(f"Error de red al consultar el modelo: {e}")

def main():
    """Bucle principal que gestiona el flujo del programa."""
    try:
        while True:
            consulta = obtener_consulta()
            if consulta:
                historial.append(consulta)
                enviar_consulta(consulta)
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")
    except Exception as e:
        print(f"Error inesperado en el programa: {e}")

if __name__ == "__main__":
    main()
