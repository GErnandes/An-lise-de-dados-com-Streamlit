import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Players',
    page_icon=':bar_chart:',
    layout='wide'
)
# Carregar os dados diretamente para verificação
df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)

# Limpar espaços em branco e caracteres invisíveis da coluna 'Club'
df_data['Club'] = df_data['Club'].astype(str).str.strip()

# Armazenar no estado da sessão
st.session_state['data'] = df_data

# Obtém uma lista de clubes únicos, ordenados pela frequência de ocorrência na coluna 'Club'
clubes = df_data['Club'].value_counts().index

# Criar o seletor de clubes
club = st.sidebar.selectbox('Clube', clubes)

df_positions = df_data[df_data['Club'] == club]
positions = df_positions['Position'].value_counts().index
position = st.sidebar.selectbox('Position', positions)

df_players= df_data[(df_data['Club'] == club) & (df_data['Position'] == position)]
players = df_players['Name'].value_counts().index
# Criar o seletor de jogador
player = st.sidebar.selectbox('Jogador', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]
st.image(player_stats['Photo'], width=150)
st.title(f"{player_stats['Name']}")

col1, col2, col3, col4= st.columns(4)
col1.markdown(f"**Clube:** {player_stats['Club']}")
col2.markdown(f"**Nacionalidade:** {player_stats['Nationality']} ")
col3.markdown(f"**Número da camisa:** {player_stats['Kit Number']:.0f}")

col1, col2, col3, col4= st.columns(4)
col1.markdown(f"**Posição:** {player_stats['Position']}")
col2.markdown(f"**Pé de preferência:** {player_stats['Preferred Foot']}")
col3.markdown(f"**Atuação de jogo:** {player_stats['Work Rate']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] /100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.1f}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))
st.subheader(f"Potencial {player_stats['Potential']}")
st.progress(int(player_stats['Potential']))

col1, col2, col3 = st.columns(3)
col1.metric(label='Valor de Mercado', value=f'£ {player_stats["Value(£)"]:,}')
col2.metric(label='Remuneração semanal', value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label='Cláusula de rescisão', value=f'£ {player_stats["Release Clause(£)"]:,}')

radar_data = pd.DataFrame({
    'Atributo': ['Reputação Internacional', 'Pé fraco', 'Habilidades'],
    'Valor': [player_stats['International Reputation'], player_stats['Weak Foot'], player_stats['Skill Moves']]
})

# Criação do gráfico de radar
fig = px.line_polar(radar_data, r='Valor', theta='Atributo', line_close=True)
fig.update_traces(fill='toself')

# Exibição do gráfico no Streamlit
st.plotly_chart(fig)

# df = pd.DataFrame({
#     'Categoria': ['A', 'B', 'C', 'D', 'E'],
#     'Valor1': [4, 3, 2, 5, 4],
#     'Valor2': [2, 3, 4, 3, 2]
# })

# # Criação do gráfico de radar
# fig = px.line_polar(df, r='Valor1', theta='Categoria', line_close=True)
# fig.add_scatterpolar(r=df['Valor2'], theta=df['Categoria'], line_close=True)

# # Exibição do gráfico no Streamlit
# st.plotly_chart(fig)# 