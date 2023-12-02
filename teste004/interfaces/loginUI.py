import streamlit as st
import time
from servico import Servico

class LoginUI():
    def Login():
        st.title("Login")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha")
        if st.button("Login"):
            user = Servico.LogarUsuario(email, senha) 
            if user is not None:
                st.success("Login realizado com sucesso")
                st.success("Bem-vindo(a), " + user.GetNome())
                st.session_state["user_id"] = user.GetId()
                st.session_state["user_nome"] = user.GetNome()
            else:
                st.error("Usuário ou senha inválido(s)")
            time.sleep(2)
            st.rerun()      
        

    def Cadastrar():
        st.title("Cadastrar")
        nome = st.text_input("Informe o seu nome")
        email = st.text_input("Informe o seu e-mail")
        senha = st.text_input("Informe a seu senha")
        if st.button("Cadastrar"):
            user = Servico.CriarUsuario(0, nome, email, senha) 
            st.success("Cadastro realizado com sucesso")
            time.sleep(2)
            st.rerun()    

   
        
