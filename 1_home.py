import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

# Inicializar o estado da sessão se não estiver presente
if 'data' not in st.session_state:
    # Carregar o DataFrame
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    
    # Converter a coluna 'Contract Valid Until' para datetime
    df_data['Contract Valid Until'] = pd.to_datetime(df_data['Contract Valid Until'], errors='coerce')
    
    # Filtrar os dados
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today()]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    

    # Armazenar o DataFrame no estado da sessão
    st.session_state['data'] = df_data

# Exibir título
st.write('# Dados oficiais do FIFA 23!')

# Barra lateral com texto
st.sidebar.markdown('teste')

# Botão para acessar dados no Kaggle
btn = st.button('Acesse os dados no Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database')

# Exibir uma descrição
st.markdown('''
Se você é um apaixonado por FIFA 23 e quer se aprofundar no universo dos jogadores do seu jogo
de futebol favorito, você chegou ao lugar certo. No [Nome do Site], 
reunimos informações detalhadas e atualizadas sobre cada atleta presente no FIFA 23, 
para que você possa aprimorar sua experiência de jogo e tomar decisões mais informadas.           
''')