import streamlit as st
from servico import Servico
import time
from modelos.usuario import Usuario

class VisitanteUI:
    def Login():
        st.title("Login")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha")
        if st.button("Login"):
            user = Servico.Logar(email, senha) 
            if user is not None:
                st.success("Login realizado com sucesso")
                st.success("Bem-vindo(a), " + user.GetNome())
                st.session_state["user_id"] = user.GetId()
                st.session_state["user_nome"] = user.GetNome()
            else:
                st.error("Emaiç ou senha inválido(s)")
            time.sleep(2)
            st.rerun()      
        

    def Cadastrar():
        st.title("Cadastrar")
        nome = st.text_input("Informe o seu nome")
        email = st.text_input("Informe o seu e-mail")
        senha = st.text_input("Informe a seu senha")
        if st.button("Cadastrar"):
            user = Usuario(0, nome, email, senha)
            Servico.InserirUsuario(user) 
            st.success("Cadastro realizado com sucesso")
            time.sleep(2)
            st.rerun()    
            