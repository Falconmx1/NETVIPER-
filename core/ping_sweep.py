import subprocess
import platform
import threading
from queue import Queue

def ping_host(ip):
    """Función para hacer ping a un host"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    
    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"  ✅ {ip} - Host activo")
            return True
        else:
            print(f"  ❌ {ip} - Inactivo")
            return False
    except:
        return False

def ping_sweep(network):
    """Escanea toda la red en busca de hosts activos"""
    print(f"\n[🐍] NETVIPER iniciando ping sweep en: {network}")
    
    # Extraer la base de la red (ej: 192.168.1.)
    base_ip = ".".join(network.split(".")[:3]) + "."
    
    threads = []
    active_hosts = []
    
    for i in range(1, 255):
        ip = base_ip + str(i)
        thread = threading.Thread(target=lambda: ping_host(ip))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(f"\n[+] Ping sweep completado")
