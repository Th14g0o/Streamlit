import streamlit as st
from Jogo import Jogo
from NJogo import NJogo #Arquivo e classe
import pandas as Panda
import time

def ListarJogos():
    st.title("Listagem de jogos")
    if(len(NJogo.Listar()) > 0):
        Dataframe = Panda.DataFrame(NJogo.Listar())
        st.table(Dataframe)
    else: st.write("Sem jogos cadastrados")

def CriarJogo():
    st.title("Adicionar jogo")
    nome = st.text_input("Digite o nome do jogo") #text_input=input de texto
    desc = st.text_area("Digite a descrição do jogo")#text_area= area de texto
    valor = st.number_input("Digite o valor")#number_input= input feito para valores numeriocos(não da para escrever letras nele)
    if st.button("Criar"):
        j = Jogo(0,nome,desc,valor)
        NJogo.Inserir(j)
        st.success("Jogo adicionado com sucesso") #se deu certo mostra mensagem
        time.sleep(2) #pausa de 2 segundos
        st.rerun()  #recarrega a pagina

def EditarJogo():
    st.title("Editar jogo")
    if(len(NJogo.Listar()) > 0):
        jogo = st.selectbox("Selecione jogo para excluir:", NJogo.Listar())
        nome = st.text_input("Digite o novo nome do jogo:", jogo.get_nome())
        desc = st.text_area("Digite a nova descrição do jogo:", jogo.get_descricao())
        valor = st.number_input("Digite o novo valor:", value=jogo.get_preco())
        if st.button("Atualizar"):
            j = Jogo(jogo.get_id(), nome, desc, valor )
            NJogo.Atualizar(j)
            st.success("Jogo atualizado com sucesso")
            time.sleep(2)
            st.rerun()
    else: st.write("Não existe nenhum jogo")
       

def ExcluirJogo():
    st.title("Excluir jogo")
    if(len(NJogo.Listar()) > 0):
        jogo = st.selectbox("Selecione jogo para excluir:", NJogo.Listar())
        if st.button("Excluir"):
            NJogo.Excluir(jogo)
            st.success("Jogo excluido com sucesso")
            time.sleep(2)
            st.rerun()
    else: st.write("Não existe nenhum jogo")
   

def BarraLateral():
    st.sidebar.header("Menu")
    pag = st.sidebar.selectbox("Pagina atual:", ["Listar","Criar", "Atualizar", "Excluir"])
    if pag == "Criar": CriarJogo()
    elif pag == "Atualizar": EditarJogo()
    elif pag == "Excluir": ExcluirJogo()
    else: ListarJogos()

def Main():
    BarraLateral()
        

Main()