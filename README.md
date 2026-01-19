# Claro Cloud Automation Lab

**Simulación de infraestructura para despliegue automatizado de servicios web.**

Este proyecto implementa una **Nube Privada** (Private Cloud) simulada en un entorno local, aplicando principios de **Infraestructura como Código (IaC)**, Virtualización y Containerización.

---

## Arquitectura e Infraestructura
El laboratorio fue diseñado bajo un esquema de **Sandbox (Entorno Aislado)** para replicar las condiciones de seguridad y operación de un servidor de producción real.

* **Host de Virtualización:** Oracle VirtualBox.
* **Sistema Operativo Guest:** Ubuntu Server 22.04 LTS (Headless / Sin interfaz gráfica).
* **Networking & Seguridad:**
    * **NAT (Network Address Translation):** Aislamiento de la red interna de la VM.
    * **Port Forwarding (Reenvío de Puertos):** Aplicación del principio de *Mínimo Privilegio*, exponiendo solo los servicios críticos:
        * `Host:2222` -> `Guest:22` (Gestión remota vía SSH).
        * `Host:8080` -> `Guest:80` (Acceso público al servicio Web).

---

## Tecnologías Utilizadas

* **Docker & Docker Compose:** Orquestación de contenedores y microservicios.
* **Nginx:** Servidor Web configurado como Reverse Proxy de alto rendimiento.
* **Python 3:** Scripting de automatización operativa (ABM) utilizando librerías `os` y `time`.
* **Linux (Bash):** Gestión de permisos, usuarios y sistema de archivos.

---

## Estructura de Archivos

* `gestion_abm.py`: Script interactivo en Python para realizar el **Alta, Baja y Monitoreo (Logs)** de la infraestructura de forma automatizada.
* `docker-compose.yml`: Archivo de orquestación que define la imagen de Nginx, el mapeo de puertos y los volúmenes.
* `index.html`: Página de inicio personalizada inyectada al contenedor mediante **Volúmenes Persistentes**.

---

## Cómo ejecutar el laboratorio

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/ariasLeonel-ing/claro-automation-lab.git](https://github.com/ariasLeonel-ing/claro-automation-lab.git)
