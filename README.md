Laboratorio UCV – Google ADK + Poetry + GitHub + SonarQube

1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un agente inteligente utilizando Google Agent Development Kit (ADK) y Python. Su finalidad es explicar conceptos tecnológicos y realizar cálculos matemáticos básicos mediante herramientas integradas en el agente.

El proyecto también aplica buenas prácticas de desarrollo de software mediante Poetry para la gestión de dependencias, Git y GitHub para el control de versiones, Pytest para las pruebas unitarias y SonarQube Cloud para el análisis de calidad del código.

2. Objetivos

Comprender el funcionamiento de un agente inteligente.

Desarrollar un agente utilizando Google ADK.

Gestionar las dependencias con Poetry.

Implementar herramientas para explicar conceptos y calcular promedios.

Realizar pruebas unitarias utilizando Pytest.

Automatizar las pruebas y el análisis de calidad mediante GitHub Actions y SonarQube Cloud.

3. Tecnologías utilizadas

Tecnología

Descripción

Python

Lenguaje de programación utilizado.

Google ADK

Framework para desarrollar agentes inteligentes.

Gemini

Modelo de inteligencia artificial utilizado por el agente.

Poetry

Administración de dependencias y entorno virtual.

Pytest

Ejecución de pruebas unitarias.

Git

Control de versiones.

GitHub

Almacenamiento y colaboración del proyecto.

GitHub Actions

Automatización de pruebas y análisis.

SonarQube Cloud

Análisis de calidad del código.

4. Funcionalidades del agente

El agente cuenta con las siguientes funcionalidades:

4.1. Explicación de conceptos tecnológicos

Mediante la herramienta explicar_concepto(), el agente puede proporcionar explicaciones de diferentes conceptos tecnológicos, entre ellos:

API.

Algoritmo.

Base de datos.

Inteligencia artificial.

Machine Learning.

Cloud Computing.

Ciberseguridad.

Internet de las cosas (IoT).

4.2. Cálculo de promedios

Mediante la herramienta calcular_promedio(), el agente puede calcular el promedio de una lista de números.

También incorpora validaciones para evitar errores cuando se proporciona una lista vacía o valores que no son numéricos.

5. Estructura del proyecto

laboratorio-adk-ucv/
│
├── .github/
│   └── workflows/
│       └── sonarqube.yml
│
├── agente_ucv/
│   ├── .adk/
│   ├── .env
│   ├── __init__.py
│   └── agent.py
│
├── test/
│   └── test_agent.py
│
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
└── sonar-project.properties

6. Instalación y configuración

Para ejecutar el proyecto se necesita tener instalado Python y Poetry.

Primero, se debe clonar el repositorio:

git clone URL_DEL_REPOSITORIO

Ingresar a la carpeta del proyecto:

cd laboratorio-adk-ucv

Instalar las dependencias:

poetry install

También se debe configurar la variable GOOGLE_API_KEY en el archivo .env, ubicado dentro de la carpeta agente_ucv.

Importante: No publicar la clave API ni compartir el archivo .env.

7. Ejecución del agente

Para iniciar el agente desde la terminal se utiliza:

poetry run adk run agente_ucv

También se puede iniciar la interfaz web con:

poetry run adk web --port 8000

Después, ingresar desde el navegador a:

http://localhost:8000

8. Pruebas unitarias

El proyecto utiliza Pytest para comprobar el funcionamiento de las herramientas implementadas.

Para ejecutar las pruebas:

poetry run python -m pytest -v

Se realizaron seis pruebas unitarias que verifican:

Explicación de un concepto conocido.

Explicación de un concepto desconocido.

Validación de un concepto vacío.

Cálculo correcto del promedio.

Validación de una lista vacía.

Validación de datos no numéricos.

Resultado: Las seis pruebas unitarias finalizaron correctamente.

9. Integración continua y análisis de calidad

El proyecto incorpora GitHub Actions para automatizar las pruebas unitarias y el análisis de calidad del código.

El flujo de trabajo se encuentra en:

.github/workflows/sonarqube.yml

Cuando se realiza un push a la rama main o se genera un pull request hacia dicha rama, se ejecutan automáticamente los siguientes pasos:

Descarga del código del repositorio.

Configuración de Python.

Instalación de Poetry.

Instalación de las dependencias.

Ejecución de las pruebas unitarias con Pytest.

Análisis del código mediante SonarQube Cloud.

La integración fue ejecutada correctamente y los pasos de pruebas y análisis finalizaron satisfactoriamente.

10. Conclusiones

Se desarrolló un agente inteligente utilizando Google ADK y Python.

Se implementaron herramientas para explicar conceptos tecnológicos y calcular promedios.

Se utilizaron validaciones para controlar entradas incorrectas.

Se aplicó Pytest para verificar el funcionamiento de las herramientas mediante pruebas unitarias.

Se utilizó Poetry para administrar las dependencias del proyecto.

Se integró GitHub Actions con SonarQube Cloud para automatizar las pruebas y el análisis de calidad del código.

Este laboratorio permitió aplicar herramientas y buenas prácticas de desarrollo de software, integrando inteligencia artificial, pruebas automatizadas y control de versiones en un mismo proyecto.