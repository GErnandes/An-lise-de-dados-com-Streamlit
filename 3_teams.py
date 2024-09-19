import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Teams',
    page_icon=':bar_chart:',
    layout='wide'
)

df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
st.session_state['data'] = df_data

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)

df_filtered = df_data[df_data['Club'] == club].set_index('Name')

st.subheader(f'Informações sobre os jogadores do clube: {club}')
st.image(df_filtered.iloc[0]['Club Logo'] ,width=150)
# st.markdown(f'## {club}')

columns = ['Age', 'Photo', 'Flag', 'Overall', 'Potential', 'Value(£)', 'Joined',
            'Wage(£)', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)' ]
st.dataframe(df_filtered[columns],
             column_config={
                 'Overall': st.column_config.ProgressColumn('Overall', format='%d', min_value=0, max_value=100),
                 'Potential': st.column_config.ProgressColumn('Potential', format='%d', min_value=0, max_value=100),
                 'Value(£)': st.column_config.NumberColumn(),
                 'Wage(£)': st.column_config.ProgressColumn('Weekly Wage', format='%d', min_value=0, max_value=df_filtered['Wage(£)'].max()),
                 'Photo': st.column_config.ImageColumn(),
                 'Flag': st.column_config.ImageColumn('Country'),
                 }, height=1000)
