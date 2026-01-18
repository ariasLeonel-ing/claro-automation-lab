import os
import time

def limpiar_pantalla():
    os.system('clear')

def mostrar_menu():
    limpiar_pantalla()
    print("========================================")
    print("   CLARO CLOUD AUTOMATION - ADMIN: LEONEL")
    print("========================================")
    print("1. [ALTA] Desplegar Servicio Cloud (Provisioning)")
    print("2. [BAJA] Dar de baja Servicio (Decommissioning)")
    print("3. [ESTADO] Ver Status de Infraestructura")
    print("4. [LOGS] Ver Logs de Acceso en tiempo real")
    print("5. Salir")
    print("========================================")

def alta():
    print("\n>>> Iniciando provisionamiento...")
    time.sleep(1)
    # Ejecuta el comando de Docker
    os.system("docker compose up -d")
    print("\n[OK] Servicio desplegado. El cliente puede acceder.")
    input("\nPresione Enter para continuar...")

def baja():
    print("\n>>> Dando de baja recursos...")
    time.sleep(1)
    os.system("docker compose down")
    print("\n[WARN] Servicio detenido. Facturación pausada.")
    input("\nPresione Enter para continuar...")

def estado():
    print("\n>>> Consultando estado del cluster...")
    os.system("docker compose ps")
    input("\nPresione Enter para continuar...")

def ver_logs():
    print("\n>>> Mostrando últimas conexiones (Ctrl+C para salir)...")
    try:
        os.system("docker compose logs -f")
    except KeyboardInterrupt:
        pass

# Loop principal
while True:
    mostrar_menu()
    opcion = input("Seleccione opción: ")

    if opcion == '1': alta()
    elif opcion == '2': baja()
    elif opcion == '3': estado()
    elif opcion == '4': ver_logs()
    elif opcion == '5':
        print("Cerrando sesión...")
        break
