import streamlit as st
import pandas as Panda
import time

from servico import Servico
from modelos.jogo import Jogo

class UsuarioUI:
    
    def ListarJogos():
        st.header("Listagem de jogos")
        if(len(Servico.ListarJogos()) > 0):
            Dataframe = Panda.DataFrame(Servico.ListarJogos())
            st.table(Dataframe)
        else: 
            st.write("Sem jogos cadastrados")

    def CriarJogo():
        st.title("Adicionar jogo")
        nome = st.text_input("Digite o nome do jogo") 
        desc = st.text_area("Digite a descrição do jogo")
        valor = st.number_input("Digite o valor")
        if st.button("Criar"):
            Servico.CriarJogo(0,nome,desc,valor)
            st.success("Jogo adicionado com sucesso") 
            time.sleep(2) 
            st.rerun()  

    def EditarJogo():
        st.title("Editar jogo")
        if(len(Servico.ListarJogos()) > 0):
            jogo = st.selectbox("Selecione jogo para excluir:", Servico.ListarJogos())
            nome = st.text_input("Digite o novo nome do jogo:", jogo.GetNome())
            desc = st.text_area("Digite a nova descrição do jogo:", jogo.GetDesc())
            valor = st.number_input("Digite o novo valor:", value=jogo.GetPrec())
            if st.button("Atualizar"):
                Servico.EditarJogo(jogo.GetId(), nome, desc, valor)
                st.success("Jogo atualizado com sucesso")
                time.sleep(2)
                st.rerun()
        else: st.write("Não existe nenhum jogo")
        

    def ExcluirJogo():
        st.title("Excluir jogo")
        if(len(Servico.ListarJogos()) > 0):
            jogo = st.selectbox("Selecione jogo para excluir:", Servico.ListarJogos())
            if st.button("Excluir"):
                Servico.RemoverJogo(jogo)
                st.success("Jogo excluido com sucesso")
                time.sleep(2)
                st.rerun()
        else: st.write("Não existe nenhum jogo")
    


 