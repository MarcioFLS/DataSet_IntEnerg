import streamlit as st
import pandas as pd


with st.container():
    st.set_page_config(page_title='Análie')
    st.subheader("Apresentação das análises explratóra")
    st.title('Análise de Dados')
    st.write('Apresentação dasAnálises de Dados')

with st.container():
    dados = pd.read_csv('interrupcoes_enel.csv')
    st.area_chart(dados, x = "DataInicioInterrupcao" , y = 'VlrIndiceEnviado')

