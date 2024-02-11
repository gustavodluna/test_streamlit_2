import streamlit as st
import plotly.express as px
import pandas as pd

# Asegúrate de tener un DataFrame 'df' cargado
df = pd.read_csv('ventas.csv',sep=";")

#print(df.head())


# Crear el gráfico de torta con Plotly Express

fig = px.pie(df, names='Genero')

#fig.show()



##################################### MAPA #####################################

import plotly.express as px
import pandas as pd
import json


 # Abre el archivo JSON
with open('data/datos.geojson', 'r') as archivo:
    counties = json.load(archivo)

    # Supongamos que tienes un DataFrame llamado 'df' con las columnas 'provincia', 'dato1', 'dato2'
df2 = pd.DataFrame({
    'provincia': ['Buenos Aires', 'Cordoba', 'Santa Fe'],
    'dato1': [100, 200, 150],
    'dato2': [50, 75, 125]
})


locs = df2['provincia'] #resumen_provincias
for loc in counties['features']:
    loc['id'] = loc['properties']['name']

fig2 = px.choropleth(df2, geojson=counties, locations='provincia', color='dato1',
                           hover_data=['dato1','dato2'],
                           labels={'dato1':'Dato uno', 'dato2':'Dato dos'},
                           title = "Mapa Coroplético",
                           color_continuous_scale="Viridis",
                           scope="south america")
fig2.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")
#fig2.show()



##########################################################################





#Streamlit de presentación, con titulo y resumen de proyecto

st.set_page_config(
    page_title="Mi Aplicación Streamlit",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

from PIL import Image
image = Image.open("data/R.jpg")
st.image(image, caption="Población", use_column_width=True)
# # Sidebar (opcional)
#st.sidebar.header("Configuración")

st.title("Análisis de Población ddasdas dsadasdas dasdsa")



st.write("""
Este proyecto tiene como objetivo analizar los datos de la población de América Latina para comprender tendencias y patrones demográficos a lo largo del tiempo. 
Se realizo el respectivo ETL y EDA de los datos preliminares. Utilizamos diversas métricas y Key Performance Indicators (KPIs) para evaluar el crecimiento poblacional, identificar tendencias y tomar decisiones informadas.
""")



# Inject custom CSS to set the width of the sidebar
st.markdown(
    """<style>
    section[data-testid="stSidebar"] {
        width: 200px !important;  # Set the width to your desired value
    }
    </style>""",
    unsafe_allow_html=True,
)

# Example sidebar content
st.sidebar.header("This is the sidebar")
st.sidebar.text("This is some text in the sidebar")

# Filtrar por países en la barra lateral
opciones_paises = st.sidebar.multiselect("Seleccione uno o varios países", df2['provincia'].unique(), default=["Santa Fe","Cordoba"])


# Filtrar los resultados de los KPIs por países seleccionados
crecimiento_filtrado = df2[df2.provincia.isin(opciones_paises)]


# Crear columnas para la presentación de los gráficos
col1, col2, col3 = st.columns([2, 0.2, 2])







##########################################################################



fig4 = px.bar(crecimiento_filtrado, x='provincia', y="dato1",color='dato1',
                           hover_data=['dato1','dato2'],
                           labels={'dato1':'Dato uno', 'dato2':'Dato dos'},
                           title = "Mapa Coroplético",
                           color_continuous_scale="Viridis",
                           width=400, 
                        height=300
                           )

#fig4.show()


##########################################################################

# Mostrar el KPI 1: Tasa de Crecimiento Anual de la Población
with col1:
    st.subheader("KPI 1: Tasa de Crecimiento de la Población Porcentual")
    st.plotly_chart(fig4)
    st.write("**Nota:** Los valores del eje y representan porcentajes.")

with col2:
# Mostrar el gráfico en la página web con Streamlit
    st.markdown("&nbsp;")


with col3:
# Mostrar el gráfico en la página web con Streamlit
    st.plotly_chart(fig2)

print("aca")
print(crecimiento_filtrado)