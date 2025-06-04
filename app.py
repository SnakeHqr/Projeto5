import streamlit as st
import pandas as pd
import plotly.express as px # type: ignore

car_data = pd.read_csv('vehicles.csv')

hist_button = st.button('Criar histograma da quilometragem')

if hist_button: # Se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros - Quilometragem')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão: preço vs. quilometragem')

if scatter_button: # Se o botão for clicado
    st.write('Criando um gráfico de dispersão: preço vs. quilometragem')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
