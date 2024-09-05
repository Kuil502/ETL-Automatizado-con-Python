# Proyecto ETL - Extracción, Transformación y Carga de Datos

Este proyecto es un pipeline ETL (Extract, Transform, Load) que extrae datos de una API, los transforma y los carga en una base de datos SQL. En caso de error al cargar los datos, se genera un respaldo en formato CSV.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes librerías de Python:

bash
pip install requests pandas sqlalchemy
Estructura del Código
El pipeline ETL se compone de tres fases principales:

Extracción de Datos: Se obtienen datos desde una API pública.
Transformación de Datos: Validación y transformación de los datos para cumplir con los requisitos.
Carga de Datos: Los datos se insertan en una base de datos SQL o se guardan en un archivo CSV en caso de error.
Cómo Ejecutar
Clona este repositorio en tu máquina local.
Asegúrate de tener Python y las librerías requeridas instaladas.
Configura la URL de la API y el motor de base de datos (SQLite en este caso) en el script principal.
Ejecuta el script:
bash
Copiar código
python main.py
