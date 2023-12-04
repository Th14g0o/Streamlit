import streamlit as st
from servico import Servico
import pandas as Panda
import time

class AdmUI:
    def ManterUsuario():
        st.title("Gerenciar Usuarios")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: AdmUI.ListarUsers()
        with tab2: AdmUI.CriarUsers()
        with tab3: AdmUI.EditarUsers()
        with tab4: AdmUI.ExcluirUsers()    

    def ListarUsers():
        st.header("Listagem:")
        if(len(Servico.ListarUsuarios()) > 0):
            DF = Panda.DataFrame(Servico.ListarUsuarios())
            st.table(DF)
        else: 
            st.write("Sem usuarios cadastrados")

    def EditarUsers():
        st.header("Edição:")

        if(len(Servico.ListarUsuarios()) > 0):
            usuario = st.selectbox("Selecione usuario para editar:", Servico.ListarUsuarios())
            nome = st.text_input("Digite o novo nome do usuario:", usuario.GetNome())
            email = st.text_input("Digite o novo email do usuario:", usuario.GetEmail())
            senha = st.text_input("Digite a nova senha:", usuario.GetSenha())
            if st.button("Atualizar"):
                Servico.EditarUsuario(usuario.GetId(), nome, email, senha)
                st.success("Usuario atualizado com sucesso")
                time.sleep(2)
                st.rerun()
        else: st.write("Não existe nenhum usuario")
        
    def CriarUsers():
        st.header("Criação:")
        nome = st.text_input("Digite o nome do usuario") 
        email = st.text_input("Digite o email do usuario")
        senha = st.text_input("Digite a senha")
        if st.button("Criar"):
            Servico.CriarUsuario(0,nome,email,senha)
            st.success("Usuario adicionado com sucesso") 
            time.sleep(2) 
            st.rerun()  
        
    def ExcluirUsers():
        st.header("Exclusão:")

        if(len(Servico.ListarUsuarios()) > 0):
            usuario = st.selectbox("Selecione usuario para excluir:", Servico.ListarUsuarios())
            if st.button("Excluir"):
                Servico.RemoverUsuario(usuario)
                st.success("Usuario excluido com sucesso")
                time.sleep(2)
                st.rerun()
        else: st.write("Não existe nenhum usuario")

    def ManterJogos():
        st.title("Gerenciar Jogos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: AdmUI.ListarJogos()
        with tab2: AdmUI.CriarJogos()
        with tab3: AdmUI.EditarJogos()
        with tab4: AdmUI.ExcluirJogos()    

    def ListarJogos():
        st.header("Listagem:")

        if(len(Servico.ListarJogos()) > 0):
            DF = Panda.DataFrame(Servico.ListarJogos())
            st.table(DF)
        else: 
            st.write("Sem jogos cadastrados")

    def EditarJogos():
        st.header("Edição:")

        if(len(Servico.ListarJogos()) > 0):
            jogo = st.selectbox("Selecione jogo para editar:", Servico.ListarJogos())
            nome = st.text_input("Digite o novo nome do jogo:", jogo.GetNome())
            desc = st.text_area("Digite a nova descrição do jogo:", jogo.GetDesc())
            valor = st.number_input("Digite o novo valor:", value=jogo.GetPrec())
            if st.button("Atualizar"):
                Servico.EditarJogo(jogo.GetId(), nome, desc, valor)
                st.success("Jogo atualizado com sucesso")
                time.sleep(2)
                st.rerun()
        else: st.write("Não existe nenhum jogo")
        
    def CriarJogos():
        st.header("Criação:")

        nome = st.text_input("Digite o nome do jogo") 
        desc = st.text_area("Digite a descrição do jogo")
        valor = st.number_input("Digite o valor")
        if st.button("Criar"):
            Servico.CriarJogo(0,nome,desc,valor)
            st.success("Jogo adicionado com sucesso") 
            time.sleep(2) 
            st.rerun()  
        
    def ExcluirJogos():
        st.header("Exclusão:")

        if(len(Servico.ListarJogos()) > 0):
            jogo = st.selectbox("Selecione jogo para excluir:", Servico.ListarJogos())
            if st.button("Excluir"):
                Servico.RemoverJogo(jogo)
                st.success("Jogo excluido com sucesso")
                time.sleep(2)
                st.rerun()
        else: st.write("Não existe nenhum jogo")




