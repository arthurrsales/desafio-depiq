import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard IGs - MDIC", layout="wide")

st.title("Exportações de Produtos com Indicação Geográfica")
st.write("Análise de dados de exportação de produtos brasileiros com registro de IG no INPI.")

@st.cache_data
def carregar_dados():
    return pd.read_csv("dados.csv")

df = carregar_dados()

# Filtro lateral
produto = st.sidebar.selectbox("Selecione o produto:", df["produto"].unique())

# Filtrar dados do produto escolhido
dados_produto = df[df["produto"] == produto]
ig_regiao = dados_produto["ig"].iloc[0]

st.subheader(f"Produto: {produto}")
st.caption(f"Região / IG: {ig_regiao}")

# Métricas principais
col1, col2 = st.columns(2)
col1.metric("Total Exportado", f"US$ {dados_produto['valor_usd'].sum():,.2f}")
col2.metric("Volume Total", f"{dados_produto['peso_kg'].sum():,.0f} kg")

st.divider()

# Gráfico de destino
fig = px.bar(
    dados_produto, 
    x="pais_destino", 
    y="valor_usd", 
    title=f"Principais países compradores de {produto}",
    labels={"pais_destino": "País", "valor_usd": "Valor (US$)"},
    color="valor_usd"
)

st.plotly_chart(fig, use_container_width=True)