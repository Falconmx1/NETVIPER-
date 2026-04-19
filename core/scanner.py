import socket
import threading
from datetime import datetime

def scan_port(ip, port):
    """Escanea un puerto específico"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"  🔓 Puerto {port} - ABIERTO")
            return port
        sock.close()
    except:
        pass
    return None

def port_scan(target, port_range):
    """Escanea un rango de puertos en un objetivo"""
    print(f"\n[🐍] NETVIPER iniciando escaneo de puertos en: {target}")
    print(f"[+] Rango: {port_range}")
    print(f"[+] Hora de inicio: {datetime.now()}\n")
    
    # Parsear rango de puertos
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
    else:
        start_port = end_port = int(port_range)
    
    # Resolver hostname a IP si es necesario
    try:
        target_ip = socket.gethostbyname(target)
        print(f"[+] Resolviendo {target} → {target_ip}")
    except:
        target_ip = target
    
    threads = []
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=lambda p=port: scan_port(target_ip, p))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(f"\n[+] Escaneo completado a las {datetime.now()}")
