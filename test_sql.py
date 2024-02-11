import streamlit as st
import mysql.connector
import pandas as pd

# Conexión a la base de datos MySQL
conn = mysql.connector.connect(
    # Configura los parámetros de conexión
    host = '186.124.175.141',
    database = 'covid',
    user = 'guti',
    password = '3138',
    port = 3306  # Puerto por defecto de MySQL
    )

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()


# Consulta SQL para contar la cantidad de registros en una tabla
query = "SELECT COUNT(sexo) FROM mi_tabla_7"

# Ejecutar la consulta SQL
cursor.execute(query)

# Obtener el resultado de la consulta
cantidad_registros = cursor.fetchone()[0]

# Imprimir la cantidad de registros
print("Cantidad de registros en la tabla:", cantidad_registros)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()