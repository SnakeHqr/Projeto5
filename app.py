import streamlit as st
import pandas as pd
import plotly.express as px # type: ignore

# --- NOVO CÓDIGO AQUI ---
st.title('Dashboard Interativo de Anúncios de Vendas de Carros')
st.write('Este dashboard interativo foi desenvolvido para explorar e visualizar dados de anúncios de vendas de veículos. Utilizando a biblioteca Streamlit, ele oferece uma interface amigável para que usuários possam analisar as características dos carros anunciados de maneira dinâmica.')
st.title('Com este aplicativo, você pode:')
st.write('''
Visualizar a distribuição da quilometragem: Entenda a frequência de veículos por diferentes faixas de quilometragem através de um histograma intuitivo.
Analisar a relação entre preço e quilometragem: Explore como o preço dos veículos se comporta em relação à sua quilometragem, identificando possíveis padrões ou tendências por meio de um gráfico de dispersão.
O aplicativo é alimentado por um conjunto de dados de veículos e busca fornecer insights rápidos sobre o mercado de carros usados, auxiliando na compreensão das variáveis que influenciam os preços e a disponibilidade.
Para começar, clique nos botões abaixo para gerar os gráficos desejados.
''')

car_data = pd.read_csv('vehicles.csv')
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
