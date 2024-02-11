import streamlit as st
import pandas as pd

from funciones import *
import plotly.express as px
import plotly.graph_objs as go

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.loaded_data = None

    def load_data(self):
        if self.loaded_data is None:
            self.loaded_data = pd.read_csv(self.file_path)
        return self.loaded_data

def main():

    saludar()
    st.title('Aplicación con Streamlit')
    st.subheader("KPI 1: Tasa de Crecimiento de la Población Porcentual")
    # Ruta del archivo CSV
    file_path = "data/df_conf.csv"

    # Crear una instancia de DataHandler
    data_handler = DataHandler(file_path)

    # Cargar los datos (solo se carga la primera vez)
    data = data_handler.load_data()

    # Mostrar los datos
    st.write(data.head())
    st.subheader("KPI 1: Tasa ")
    casos_confirmados,total_muertes,let=indicadores(data)
    st.plotly_chart(casos_confirmados)

if __name__ == '__main__':
    main()
