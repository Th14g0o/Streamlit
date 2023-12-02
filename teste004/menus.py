import streamlit as st
import time
from servico import Servico
from interfaces.usuarioUI import UsuarioUI
from interfaces.loginUI import LoginUI

class Menus:
    def MenuVisitante():
        st.sidebar.header("Menu")
        op = st.sidebar.selectbox("Pagina atual:", ["Login", "Abrir Conta"])
        if op == "Login":
            LoginUI.Login()
        if op == "Abrir Conta": 
            LoginUI.Cadastrar()


    def MenuUsuario():
        st.sidebar.header("Menu")
        pag = st.sidebar.selectbox("Pagina atual:", ["Listar","Criar", "Atualizar", "Excluir"])
        if pag == "Criar": 
            UsuarioUI.CriarJogo()
        elif pag == "Atualizar": 
            UsuarioUI.EditarJogo()
        elif pag == "Excluir": 
            UsuarioUI.ExcluirJogo()
        else: 
            UsuarioUI.ListarJogos()

    def Deslogar():
        if st.sidebar.button("Deslogar"):
            del st.session_state["user_id"]
            del st.session_state["user_nome"]
            st.rerun()

    def BarraLateral():
        if "user_id" not in st.session_state:
            Menus.MenuVisitante()   
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["user_nome"])
            if st.session_state["user_nome"] == "admin": 
                #Menus.menu_admin()
                pass
            else: 
                Menus.MenuUsuario()
            Menus.Deslogar()  

    def Main():
        Servico.IniciarAdm()
        Menus.BarraLateral()

Menus.Main()