import requests
import pandas as pd
from sqlalchemy import create_engine
import os

# Paso 1: Extraer datos de una API
def extract_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Levanta una excepción para códigos de error HTTP
        data = response.json()
        print("Extracción exitosa.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error en la extracción de datos: {e}")
        return None

# Paso 2: Transformar datos y validarlos
def transform_data(data):
    try:
        df = pd.DataFrame(data)
        
        # Validaciones de columnas necesarias
        required_columns = ['column1', 'column2']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Faltan columnas necesarias: {required_columns}")
        
        # Transformaciones adicionales
        df['new_column'] = df['column1'] * df['column2']
        
        # Análisis estadístico preliminar
        analysis = df.describe()  # Análisis básico: count, mean, std, min, etc.
        print("Análisis preliminar:")
        print(analysis)
        
        return df
    except ValueError as e:
        print(f"Error en la transformación de datos: {e}")
        return None

# Paso 3: Cargar los datos en una base de datos SQL
def load_data(df, db_engine, table_name):
    try:
        df.to_sql(table_name, con=db_engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en la tabla {table_name}.")
    except Exception as e:
        print(f"Error al cargar los datos en la base de datos: {e}")
        # Respaldo en CSV en caso de error
        backup_path = os.path.join(os.getcwd(), 'backup.csv')
        df.to_csv(backup_path, index=False)
        print(f"Datos respaldados en {backup_path}.")

# Ejecución del ETL
if __name__ == "__main__":
    url = 'https://api.example.com/data'
    engine = create_engine('sqlite:///mydatabase.db')

    # Extraer datos
    data = extract_data(url)
    
    if data:  # Continuar si la extracción fue exitosa
        # Transformar datos
        df = transform_data(data)
        
        if df is not None:  # Continuar si la transformación fue exitosa
            # Cargar datos en la base de datos
            load_data(df, engine, 'my_table')
