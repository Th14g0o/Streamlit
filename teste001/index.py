import streamlit as st
import pandas as pd #importei pra tabela

st.title("Teste de Instalação do Streamlit | Elementos")
st.write("Se o Streamlit foi instalado corretamente, você verá esta mensagem.")
st.write("")

st.markdown("## Botão")
if st.button("Clique-me"):
    st.write("Você clicou no botão!")
st.write("")

st.markdown("## Caixa de seleção")
selected_option = st.selectbox("Selecione uma opção", ["Opção 1", "Opção 2", "Opção 3"])
st.write("Você selecionou:", selected_option)

st.write("")
st.markdown("## Slider")
valor = st.slider("Selecione um valor", 0, 100, 50)
st.write(f"Valor selecionado: {valor}")

st.write("")
st.markdown("## Check Box")
if st.checkbox("Mostrar Caixa de texto"):
    #input text
    st.markdown("### Caixa de texto")
    user_input = st.text_input("Digite algo")
    st.write(f"Você digitou: {user_input}")

st.write("")
st.markdown("## Caixa de multipla seleção")
opcoes_selecionadas = st.multiselect("Escolha várias opções", ["Opção 1", "Opção 2", "Opção 3"])
st.write("Você selecionou:", opcoes_selecionadas)

st.write("")
st.markdown("## Coluna 1 e 2")
col1, col2 = st.columns(2)
col1.write("Isso está na coluna 1.")
col2.write("Isso está na coluna 2.")

st.write("")
# Lista simples
st.markdown("## Lista simples")
st.write("Lista de itens:")
st.write("- Item 1")
st.write("- Item 2")
st.write("- Item 3")


st.write("")
st.markdown("## Tabela")

nomes = ['Alice', 'Bob', 'Charlie']
idades= [25, 30, 35]
cidades = ['A', 'B', 'C']
indices = ['-', '+', '/']
# Dados para a tabela
dados = {
    'Nome': nomes,
    'Idade': idades,
    'Cidade': cidades
}
# Criando um DataFrame do Pandas
df = pd.DataFrame(dados)
# Exibindo a tabela no Streamlit
st.table(df)

# Criando um DataFrame do Pandas com índice personalizado
df = pd.DataFrame(dados, index=indices)
st.table(df)



st.sidebar.title("Barra lateral")
st.sidebar.markdown("## Caixa de seleção na lateral")
option = st.sidebar.selectbox("Selecione uma opção", ["Opção 4", "Opção 5", "Opção 6"])
