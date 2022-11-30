import streamlit as st
from sistemas import entradas,saidas

st.set_page_config(
    page_title= "Sistema de Estoque",
    initial_sidebar_state="collapsed",
)

st.sidebar.title('Menu')

main_page = st.sidebar.button('Inicio')

st.sidebar.header('Controle de Estoque')
opa = st.sidebar.selectbox('Funções',['Entradas','Saidas'])

st.sidebar.header('Analise Financeira')
opb = st.sidebar.selectbox('Financeiro',['Ativos','Passivos'])


if opa == 'Entradas':
    entradas.entradas()
elif opa == 'Saidas':
    saidas.saidas()

style =  """
    <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        header{visibility:hidden;}
    </style>
"""
st.markdown(style,unsafe_allow_html=True)