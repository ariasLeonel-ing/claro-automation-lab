# Claro Cloud Automation Lab

Simulación de infraestructura para despliegue automatizado de servicios web.

## Arquitectura e Infraestructura
Este laboratorio simula una **Nube Privada** desplegada en un entorno controlado (Sandbox), replicando las condiciones de un servidor de producción.

* **Host:** Oracle VirtualBox.
* **Sistema Operativo:** Ubuntu Server 22.04 LTS (Headless).
* **Networking:**
    * Configuración de red mediante **NAT** para aislamiento de seguridad.
    * Reglas de **Port Forwarding** para exponer servicios específicos:
        * `Host:2222` -> `Guest:22` (Gestión SSH).
        * `Host:8080` -> `Guest:80` (Servicio Web Nginx).

Tecnologías
- **Docker & Docker Compose**
- **Nginx** (Reverse Proxy)
- **Python** (Script de Automatización ABM)
- **Ubuntu Server**

Archivos
- `gestion_abm.py`: Script interactivo para Alta/Baja de contenedores.
- `docker-compose.yml`: Orquestación del servicio web.
- `index.html` : Página de inicio personalizada (Volumen persistente).
---
*Developed by Leonel Arias*
