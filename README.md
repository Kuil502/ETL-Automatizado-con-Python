# Proyecto ETL - Extracción, Transformación y Carga de Datos

Este proyecto es un pipeline ETL (Extract, Transform, Load) que extrae datos de una API, los transforma y los carga en una base de datos SQL. En caso de error al cargar los datos, se genera un respaldo en formato CSV.

## Tabla de contenidos

- [Requisitos](#requisitos)
- [Estructura del Código](#estructura-del-código)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Explicación de Funcionalidades](#explicación-de-funcionalidades)
- [Respaldo de Datos](#respaldo-de-datos)
- [Licencia](#licencia)

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
Explicación de Funcionalidades
Paso 1: Extracción de Datos
La función extract_data(api_url) utiliza la librería requests para obtener los datos en formato JSON desde una API. Si ocurre algún error durante la extracción, se maneja una excepción para evitar que el programa falle.

python
Copiar código
def extract_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Verifica códigos de estado HTTP
        data = response.json()
        print("Extracción exitosa.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error en la extracción de datos: {e}")
        return None
Paso 2: Transformación de Datos
La función transform_data(data) transforma el JSON en un DataFrame de Pandas. Luego se validan columnas necesarias y se realizan transformaciones adicionales, como agregar nuevas columnas derivadas de las existentes. Finalmente, se ejecuta un análisis estadístico preliminar.

python
Copiar código
def transform_data(data):
    df = pd.DataFrame(data)
    df['new_column'] = df['column1'] * df['column2']  # Ejemplo de transformación
    analysis = df.describe()
    return df
Paso 3: Carga de Datos
Los datos transformados se cargan en una base de datos SQL utilizando SQLAlchemy. Si ocurre un error, los datos se respaldan en un archivo CSV.

python
Copiar código
def load_data(df, db_engine, table_name):
    try:
        df.to_sql(table_name, con=db_engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en {table_name}.")
    except Exception as e:
        df.to_csv('backup.csv', index=False)
        print(f"Error al cargar los datos. Respaldo en CSV creado.")
Respaldo de Datos
Si ocurre algún error al cargar los datos en la base de datos, se guarda un archivo CSV como respaldo en el directorio de trabajo actual.

Licencia
Este proyecto está bajo la Licencia MIT. Puedes consultarla aquí.

css
Copiar código

Este archivo proporciona una documentación clara y concisa para tu código, explicando cada paso del proceso ETL. Si necesitas modificar algo, avísame.
