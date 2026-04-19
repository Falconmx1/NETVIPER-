#!/usr/bin/env python3
# NETVIPER - La serpiente de tus redes
# Multiplataforma: Linux / Windows

import argparse
import sys
import platform
from core.scanner import port_scan
from core.ping_sweep import ping_sweep
from core.stealth import stealth_mode

def banner():
    print("""  
    ╔═══════════════════════════════════════╗
    ║  🐍⚡   N E T V I P E R   ⚡🐍        ║
    ║  "Pica y domina la red"               ║
    ╚═══════════════════════════════════════╝
    """)

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="NETVIPER - Herramienta de reconocimiento de red")
    parser.add_argument("--scan", help="Escanea una red (ejemplo: 192.168.1.0/24)")
    parser.add_argument("--ports", help="Rango de puertos a escanear (ejemplo: 1-1000)")
    parser.add_argument("--stealth", action="store_true", help="Modo sigiloso")
    parser.add_argument("--sniff", action="store_true", help="Intercepta tráfico (próximamente)")
    parser.add_argument("--ping-sweep", help="Descubre hosts vivos en una red (ejemplo: 192.168.1.0/24)")
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    print(f"[+] Sistema operativo detectado: {platform.system()}")
    
    if args.stealth:
        stealth_mode()
    
    if args.ping_sweep:
        ping_sweep(args.ping_sweep)
    
    if args.scan:
        port_range = args.ports if args.ports else "1-1000"
        port_scan(args.scan, port_range)

if __name__ == "__main__":
    main()
