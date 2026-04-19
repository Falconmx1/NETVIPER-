import time
import random

def stealth_mode():
    """Activa el modo sigiloso"""
    print("\n[🐍] Modo sigiloso ACTIVADO")
    print("[!] Reduciendo velocidad de escaneo para evitar detección...")
    print("[!] Inyectando delays aleatorios entre paquetes...\n")
    
    # Simular configuración de stealth
    time.sleep(random.uniform(0.5, 1.5))
    print("[+] Técnicas de stealth aplicadas:")
    print("    - Randomización de tiempos entre paquetes")
    print("    - Reducción de tasa de paquetes por segundo")
    print("    - Modo 'slow scan' activado\n")
