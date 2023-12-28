import streamlit as st
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt


with st.container():
    # st.set_page_config(page_title='Análie') Precisa corrigir!
    st.subheader("Apresentação das análises explratóra")
    st.title('Análise de Dados')
    st.write('Interrupções de energia elétrica no nordeste')
    int_enel = pd.read_csv('interrupcoes_enel.csv')
    int_enel

with st.container():
    # Unidades consumidoras
    st.write('Unidades')
    dados = pd.read_csv('interrupcoes_enel.csv')
    q_nunic = int_enel[['DscConjuntoUnidadeConsumidora', 'NumUnidadeConsumidora']]
    q_nunic
    soma = int_enel['NumUnidadeConsumidora'].sum()
    st.text_area('A soma é: ', soma)
    desc = int_enel['NumUnidadeConsumidora'].describe()
    desc
    mediana = int_enel['NumUnidadeConsumidora'].median()
    st.text_area('A mediana é: ', mediana)
    st.area_chart(dados, x = "DscConjuntoUnidadeConsumidora" , y = 'NumUnidadeConsumidora')

    
with st.container():
    st.write('Consumidores')
    dados = pd.read_csv('interrupcoes_enel.csv')
    c_nunic = int_enel[['DscConjuntoUnidadeConsumidora', 'NumConsumidorConjunto']]
    c_nunic
    soma = int_enel['NumConsumidorConjunto'].sum()
    st.text_area('A soma é: ', soma)
    desc = int_enel['NumConsumidorConjunto'].describe()
    desc
    mediana = int_enel['NumConsumidorConjunto'].median()
    st.text_area('A mediana é: ', mediana)
    st.area_chart(dados, x = "DscConjuntoUnidadeConsumidora" , y = 'NumConsumidorConjunto')

with st.container():
    st.write('Índices')
    dados = pd.read_csv('interrupcoes_enel.csv')
    q_ind = int_enel[['DataInicioInterrupcao', 'VlrIndiceEnviado']]
    q_ind
    soma = int_enel['VlrIndiceEnviado'].sum()
    st.text_area('A soma é: ', soma)
    desc = int_enel['VlrIndiceEnviado'].describe()
    desc
    mediana = int_enel['VlrIndiceEnviado'].median()
    st.text_area('A mediana é: ', mediana)
    st.area_chart(dados, x = "DataInicioInterrupcao" , y = 'VlrIndiceEnviado')

with st.container():
    st.write('Nulos')
    nulos = int_enel.isnull()
    nulos


with st.container():
    dados = pd.read_csv('interrupcoes_enel.csv')

    x = int_enel[['DscSubestacaoDistribuicao', 'NumUnidadeConsumidora']].groupby('DscSubestacaoDistribuicao').mean().sort_values(by=['NumUnidadeConsumidora']).head(5).index
    y = int_enel[['DscSubestacaoDistribuicao', 'NumUnidadeConsumidora']].groupby('DscSubestacaoDistribuicao').mean().sort_values(by=['NumUnidadeConsumidora']).head(5).values
    plt.scatter(x,y)
    plt.show()
    

 