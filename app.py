#es un bloc de notas que ejecuta todo el codigo
import streamlit as st
import pandas as pd
import plotly.express as px
#aqui se prepara todo para el sitio web

#Leer el archivo CSV
pokemon = pd.read_csv(r'C:\Users\Fer Titla\Desktop\TripleTen\sprint_7_tripleten\pokemon.csv')
pokemon.head()#leer DF completo

#Crear el contenido de la aplicación basada en streamlit

#Encabezado con st.header()
# Configuración básica de la página
st.set_page_config(
    page_title="Pokémon Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Título principal del proyecto
st.title("📊 Pokémon Analytics Dashboard")

st.subheader(
    "Exploración, limpieza y visualización interactiva de métricas clave del universo Pokémon"
)

# Separador
st.divider()

# Sección: Descripción del proyecto
st.header("📌 Descripción del Proyecto")

st.markdown(
    """
    Este dashboard presenta un análisis exploratorio del dataset de Pokémon,
    enfocado en métricas de **captura**, **atributos físicos** y **desempeño en combate**.

    El objetivo es demostrar un flujo completo de trabajo en análisis de datos:
    - Limpieza y normalización del dataset  
    - Análisis exploratorio (EDA)  
    - Visualizaciones interactivas con Plotly  
    - Presentación de insights mediante Streamlit  

    📌 **Caso de uso equivalente empresarial**:  
    Segmentación de productos o usuarios según dificultad de adquisición,
    características clave y rendimiento.
    """
)

# Separador visual
st.divider()


#Crear un botón que, al hacer clic en él, construya un histograma 
#Para hacerlo, considera utilizar las funciones [st.write()] y [st.plotly_chart()].

st.header("📊 Histograma de Capture Rate")

# Botón
if st.button("Mostrar histograma"):
    
    st.write("Distribución del Capture Rate de los Pokémon")

    # Crear el histograma
    fig = px.histogram(
        pokemon,
        x='capture_rate',
        nbins=30,
        title='Distribución del Capture Rate'
    )

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)


#Agrega otro botón que, al hacer clic en él, construya un gráfico de dispersión

# Botón para mostrar scatter plot
if st.button("Mostrar gráfico de dispersión"):
    
    st.write("Relación entre el peso y la fuerza de ataque de los Pokémon")

    # Limpiar filas necesarias para el scatter
    df_scatter = pokemon.dropna(subset=['weight_kg', 'attack', 'type1', 'capture_rate'])

    df_scatter ['capture_rate'] =  df_scatter ['capture_rate'].astype(str).str.extract(r'(\d+)').astype(float)               # convierte a número

    # Crear el gráfico de dispersión
    fig = px.scatter(
        df_scatter,
        x='weight_kg',
        y='attack',
        color='type1',
        size='capture_rate',
        title='Peso vs Fuerza de Ataque de los Pokémon',
        labels={
            'weight_kg': 'Peso (kg)',
            'attack': 'Fuerza (Attack)',
            'type1': 'Tipo',
            'capture_rate': 'Capture Rate'
        },
        opacity=0.7
    )

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)



#Agrega una casilla de verificación
#Puedes pedirle al usuario o la usuaria que seleccione una casilla de verificación 
#correspondiente a un histograma o un diagrama de dispersión y luego 
# generar un gráfico basado en la casilla de verificación seleccionada. 

st.header("📊 Selección de visualización")

st.write("Selecciona el tipo de gráfico que deseas visualizar:")

# Casillas de verificación
mostrar_histograma = st.checkbox("Mostrar histograma de Capture Rate")
mostrar_scatter = st.checkbox("Mostrar gráfico de dispersión (Peso vs Ataque)")

# Histograma
if mostrar_histograma:
    
    st.write("Distribución del Capture Rate de los Pokémon")

    fig_hist = px.histogram(
        pokemon,
        x='capture_rate',
        nbins=30,
        title='Distribución del Capture Rate'
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if mostrar_scatter:
    
    st.write("Relación entre el peso y la fuerza de ataque de los Pokémon")

    df_scatter = pokemon.dropna(
        subset=['weight_kg', 'attack', 'type1', 'capture_rate']
    )
    df_scatter ['capture_rate'] =  df_scatter ['capture_rate'].astype(str).str.extract(r'(\d+)').astype(float)               # convierte a número

    fig_scatter = px.scatter(
        df_scatter,
        x='weight_kg',
        y='attack',
        color='type1',
        size='capture_rate',
        title='Peso vs Fuerza de Ataque de los Pokémon',
        labels={
            'weight_kg': 'Peso (kg)',
            'attack': 'Fuerza (Attack)',
            'type1': 'Tipo',
            'capture_rate': 'Capture Rate'
        },
        opacity=0.7
    )

    st.plotly_chart(fig_scatter, use_container_width=True)