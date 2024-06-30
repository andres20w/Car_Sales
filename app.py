import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("/Users/Usuario/Documents/Proyectos/Car_Sales/vehicles_us.csv")
car_data['model_year'] = car_data['model_year'].fillna('')
car_data['model_year'] = car_data['model_year'].astype('str')
car_data['cylinders'] = car_data['cylinders'].fillna(0)
car_data['cylinders'] = car_data['cylinders'].astype('int')
car_data['odometer'] = car_data['odometer'].fillna(0)
car_data['odometer'] = car_data['odometer'].astype('int')
car_data['paint_color'] = car_data['paint_color'].fillna("Not available")
car_data['is_4wd'] = car_data['is_4wd'].fillna("No")
car_data['is_4wd'] = car_data['is_4wd'].replace(1, "Yes")

st.header('Venta de los mejores autos usados')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos, que muestra la cantidad de vehículos según su número de cilindros:')
    fig = px.histogram(car_data, x="cylinders")
    st.plotly_chart(fig, use_container_width=True)
    
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')
if scatter_checkbox:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de autos, en el que se compara su año de fabricación y rango de precio:')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
    fig.show()

