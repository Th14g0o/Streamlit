import streamlit as st

#cada função é uma pagina diferente
def pagina_inicio():
    st.title("Página Inicial")
    st.write("Bem-vindo à página inicial!")

def pagina_sobre():
    st.title("Página Sobre")
    st.write("Esta é a página sobre.")

# Caixa de seleção sendo usada para navegação
pagina_selecionada = st.sidebar.selectbox("Selecione uma página", ["Início", "Sobre"])

# Determina qual página exibir com base na seleção do usuário
if pagina_selecionada == "Início":
    pagina_inicio()
elif pagina_selecionada == "Sobre":
    pagina_sobre()