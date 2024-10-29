# gestion_proyectos_mineros

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada en Python utilizando el framework Flask. Su propósito es gestionar proyectos mineros, permitiendo a los usuarios crear solicitudes, asignar tareas, ingresar datos, comparar datos con históricos, generar alertas y notificaciones, y generar reportes.

## Configuración y Ejecución del Proyecto

### Requisitos

- Python 3.8 o superior
- Flask
- SQLAlchemy

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/simon-gonzalez/gestion_proyectos_mineros.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd gestion_proyectos_mineros
   ```
3. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
4. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Inicia el servidor Flask:
   ```bash
   flask run
   ```
2. Abre tu navegador y navega a `http://127.0.0.1:5000` para ver la aplicación en funcionamiento.

## Contribuir al Proyecto

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en este repositorio.
