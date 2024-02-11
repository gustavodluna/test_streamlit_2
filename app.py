import streamlit as st
import plotly.express as px
import pandas as pd

from funciones import saludar, indicadores


saludar()
#Streamlit de presentación, con titulo y resumen de proyecto

st.set_page_config(
    page_title="Mi Aplicación Streamlit",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)


# Localizacion del archivo
file_location_df = "data/df.csv"
file_location_resumen_provincias = "data/resumen_provincias.csv"
file_location_resumen_diagnostico = "data/resumen_diagnostico.csv"
file_location_df_fallecidos = "data/df_fallecidos.csv"
file_location_resumen_diagnostico_mes = "data/resumen_diagnostico_mes.csv"


import streamlit as st

@st.cache_data
def load_data():
    
    resumen_provincias=pd.read_csv(file_location_resumen_provincias)
    resumen_diagnostico=pd.read_csv(file_location_resumen_diagnostico)
    df_fallecidos=pd.read_csv(file_location_df_fallecidos)
    resumen_diagnostico_mes=pd.read_csv(file_location_resumen_diagnostico_mes)
    return resumen_provincias, resumen_diagnostico, df_fallecidos, resumen_diagnostico_mes

resumen_provincias, resumen_diagnostico, df_fallecidos, resumen_diagnostico_mes = load_data()




# Inject custom CSS to set the width of the sidebar
st.markdown(
    """<style>
    section[data-testid="stSidebar"] {
        width: 300px !important;  # Set the width to your desired value
    }
    </style>""",
    unsafe_allow_html=True,
)

# Example sidebar content
st.sidebar.header("This is the sidebar")
st.sidebar.text("This is some text in the sidebar")

# Filtrar por países en la barra lateral
opciones_paises = st.sidebar.multiselect("Seleccione uno o varios países", resumen_provincias['provincia'].unique(), default=["Santa Fe","Cordoba","Buenos Aires","Salta"])








##################################### MAPA #####################################

import plotly.express as px
import pandas as pd
import json



# Filtrar los resultados de los KPIs por países seleccionados
provincias_filtrado = resumen_provincias[resumen_provincias.provincia.isin(opciones_paises)]

 # Abre el archivo JSON
with open('data/datos.geojson', 'r') as archivo:
    counties = json.load(archivo)


locs = resumen_provincias['provincia'] #resumen_provincias
for loc in counties['features']:
    loc['id'] = loc['properties']['name']

fig2 = px.choropleth(provincias_filtrado, geojson=counties, locations='provincia', color='casos_confirmados',
                           hover_data=["casos_confirmados","cantidad_fallecidos","cuidado_intensivo","asistencia_respiratoria_mecanica"],
                           
                     #labels={'dato1':'Dato uno', 'dato2':'Dato dos'},
                           title = "Mapa Coroplético",
                           color_continuous_scale="Viridis",
                           scope="south america",
                    height=600,
                    width=400)

fig2.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")
fig2.update_traces(hovertemplate='<b>%{location}</b><br>' +
                   'Casos confirmados: %{customdata[0]:,.0f}<br>' +
                   'Cantidad de fallecidos: %{customdata[1]:,.0f}<br>' +
                   'Cuidado intensivo: %{customdata[2]:,.0f}<br>' +
                   'Asistencia respiratoria mecánica: %{customdata[3]:,.0f}<br>')




##########################################################################







from PIL import Image
image = Image.open("data/R.jpg")
st.image(image, caption="Población", use_column_width=True)
# # Sidebar (opcional)
#st.sidebar.header("Configuración")

# Crear una aplicación de Streamlit
st.title("Análisis de Población - KPIs")
st.write("""
Este proyecto tiene como objetivo analizar los datos de la población de América Latina para comprender tendencias y patrones demográficos a lo largo del tiempo. 
Se realizo el respectivo ETL y EDA de los datos preliminares. Utilizamos diversas métricas y Key Performance Indicators (KPIs) para evaluar el crecimiento poblacional, identificar tendencias y tomar decisiones informadas.
""")


st.divider()



st.title("Análisis de Población ddasdas dsadasdas dasdsa")









# Crear columnas para la presentación de los gráficos
col1, col2, col3 = st.columns([2, 0.2, 2])







##########################################################################

# Filtrar los resultados de los KPIs por países seleccionados
provincias_filtrado = resumen_provincias[resumen_provincias.provincia.isin(opciones_paises)]


letalidad = px.bar(provincias_filtrado.sort_values(by="tasa_letalidad_%",ascending=False), x='provincia', y="tasa_letalidad_%",color='tasa_letalidad_%',
                           #hover_data=['dato1','dato2'],
                           #labels={'dato1':'Dato uno', 'dato2':'Dato dos'},
                           title = "Tasa de letalidad",
                           color_continuous_scale="Viridis",
                           width=400, 
                        height=300
                           )


##########################################################################


# Crear un gráfico de barras en Plotly
def barras_estado_por_mes_grafico(df):
    #resumen_diagnostico_mes
    fig = px.bar(df, x="fecha_diagnostico", y=["asistencia_respiratoria_mecanica","cuidado_intensivo", "cantidad_fallecidos"], labels={"fecha_diagnostico": "Mes y Año"})
    fig.update_layout(
        xaxis_title="Mes y Año",
        yaxis_title="Total",
        title="Situacion por Mes y Año"
    )
    return fig


##########################################################################

xd=barras_estado_por_mes_grafico(resumen_diagnostico_mes)

# Mostrar el KPI 1: Tasa de Crecimiento Anual de la Población
with col1:
    st.subheader("KPI 1: Tasa de Crecimiento de la Población Porcentual")
    st.plotly_chart(letalidad)
    st.write("**Nota:** Los valores del eje y representan porcentajes.")

with col2:
# Mostrar el gráfico en la página web con Streamlit
    st.markdown("&nbsp;")
   

##########################################################################



##########################################################################

with col3:

    st.subheader("KPI 1: Tasa de Crecimiento de la Población Porcentual")
    
    
# Mostrar el gráfico en la página web con Streamlit
    st.plotly_chart(fig2)
    st.write("**Nota:** Los valores del eje y representan porcentajes.")
# Crear nuevas columnas para presentar más gráficos
col4, col5, col6 = st.columns([2, 0.2, 2])

with col4:

    st.subheader("KPI 1: Tasa de Crecimiento de la Población Porcentual")
    
    
# Mostrar el gráfico en la página web con Streamlit
    st.plotly_chart(xd)
    st.write("**Nota:** Los valores del eje y representan porcentajes.")