import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st


# função que carrega o dataset
def carregar_dataset(nome_dataset):
    return sns.load_dataset(nome_dataset)


# CORPO
## CORPO - Título da Aplicação
st.markdown("""
            # iNalyze
            ### *Sua ferramenta de análise de dados*
            ---
            """)

## CORPO - Carregando o dataset
nome_dataset = st.text_input('Qual o nome do dataset?', value = 'penguins')
if nome_dataset:
    df = carregar_dataset(nome_dataset)

        
# SIDEBAR
## SIDEBAR - Filtro dos campos
with st.sidebar:
    st.title('Filtros')
    cols_selected = st.multiselect('Filtre os campos que deseja para a análise:',
                                   options = list(df.columns),
                                   default = list(df.columns))

# filtra os campos selecionados
df_selected = df[cols_selected]
    
    
## CORPO - Info do dataset

with st.expander('Dados do dataset'):
    st.header('Dados do dataset')
    st.subheader('Primeiros Registros')
    st.write(df_selected.head())

    st.subheader('Colunas')
    for col in df_selected.columns:
        st.markdown(f'- {col}')

    st.subheader('Dados Faltantes')
    st.write(df_selected.isna().sum()[df_selected.isna().sum() > 0])

    st.subheader('Estatística Descritiva')
    st.write(df_selected.describe())

## CORPO - Análise Univariada
st.header('Análise Univariada')
univar_campo = st.selectbox('Selecione um campo numérico para avaliar sua distribuição:',
             options = df_selected.select_dtypes(include = np.number).columns)
st.plotly_chart(px.histogram(data_frame = df_selected, x = univar_campo))
st.plotly_chart(px.box(data_frame = df_selected, y = univar_campo))


## CORPO - Análise Bivariada


### CORPO - Análise Bivariada - gráfico de dispersão

        
### CORPO - Análise Bivariada - gráfico de boxplot


### CORPO - Análise Bivariada - gráfico de pairplot

    


# ATIVIDADES
# Refatore o código, aplicando as modificações:

# 1 - Modularize o código passando a função "carrega_dataset" para um módulo

# 2 - Crie um slider no sidebar que permita filtrar uma amostra do dataset.
#     Para realizar amostragem, utilize o método sample do dataframe pandas.

# 3 - Adicione a informação do tamanho do dataset na seção 
#     de 'Dados do Dataset'

# 4 - Adicione uma seção de análise multivariada:
#   4.1 - Adicione a possibilidade de segmentação no gráfico de dispersao
#   4.2 - Adicione checkbox que permita incluir linha de tendência 
#         no gráfico de dispersão
#   4.3 - Adicione a possibilidade de segmentação no gráfico de boxplot
#   4.4 - Adicione a possibilidade de segmentação no gráfico de pairplot
