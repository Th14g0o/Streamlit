import streamlit as st
from interfaces.visitanteUI import VisitanteUI
from interfaces.usuarioUI import UsuarioUI

class Menu:
    def MenuVisitante():
        st.sidebar.header("Menu Visitante")
        op = st.sidebar.selectbox("Pagina atual:", ["Login", "Cadastro"])
        if op ==  "Cadastro":
            VisitanteUI.Cadastrar()
        else:
            VisitanteUI.Login()

    def MenuUsuario():
        st.sidebar.header("Menu Usuario")
        op = st.sidebar.selectbox("Pagina atual:", ["Meus Contatos", "Meus Grupos"])
        if op ==  "Meus Grupos":
            UsuarioUI.Grupos()
        else:
            UsuarioUI.Contatos()

    def Deslogar():
        if st.sidebar.button("Deslogar"):
            del st.session_state["user_id"]
            del st.session_state["user_nome"]
            st.rerun()

    def BarraLateral():
        if "user_id" not in st.session_state:
            Menu.MenuVisitante()   
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["user_nome"])
            Menu.MenuUsuario()
            Menu.Deslogar() 

Menu.BarraLateral()