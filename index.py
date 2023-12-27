import streamlit as st
import pandas as pd


with st.container():
    # st.set_page_config(page_title='Análie') Precisa corrigir!
    st.subheader("Apresentação das análises explratóra")
    st.title('Análise de Dados')
    st.write('Apresentação dasAnálises de Dados')
    int_enel = pd.read_csv('interrupcoes_enel.csv')

with st.container():
    int_enel = pd.read_csv('interrupcoes_enel.csv')
    int_enel



with st.container():
    dados = pd.read_csv('interrupcoes_enel.csv')
    st.area_chart(dados, x = "DataInicioInterrupcao" , y = 'VlrIndiceEnviado')

with st.container():
    dados = pd.read_csv('interrupcoes_enel.csv')
    st.area_chart(dados, x = "DataInicioInterrupcao" , y = 'NumUnidadeConsumidora')

with st.container():
    dados = pd.read_csv('interrupcoes_enel.csv')
    st.area_chart(dados, x = "NumConsumidorConjunto" , y = 'NumConsumidorConjunto')

with st.container():
    soma = int_enel['NumUnidadeConsumidora'].sum()
    st.text_area('A soma é: ', soma)

 