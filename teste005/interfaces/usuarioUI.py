import streamlit as st
from modelos.usuario import Usuario
from modelos.grupo import Grupo
from modelos.contato import Contato
from modelos.membro import Membro
from servico import Servico
import pandas as pd
import time

class UsuarioUI:
    def Contatos():
        st.title("Contatos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: UsuarioUI.ListarContatos()
        with tab2: UsuarioUI.CriarContato()
        with tab3: UsuarioUI.EditarContato()
        with tab4: UsuarioUI.ExcluirContato()    

    def ListarContatos():
        st.header("Seus contatos")
        if (len(Servico.ListarMeusContato(st.session_state["user_id"])) > 0):
            df = pd.DataFrame(Servico.ListarMeusContato(st.session_state["user_id"]))
            st.table(df)
        else: st.write("Você não cadastrou nenhum contato")

    def CriarContato():
        st.header("Adicionar contato")
        if (len(Servico.ListarUsuariosQueNaoAdicioneiComoContato(st.session_state["user_id"])) > 0):
            u = st.selectbox("Escolha um contato para adicionar", Servico.ListarUsuariosQueNaoAdicioneiComoContato(st.session_state["user_id"]))
            nome = st.text_input("Digite o nome do contato")
            if st.button("Adicionar"):
                c = Contato(0, u.GetId(), st.session_state["user_id"], nome)
                Servico.InserirContato(c)
                st.success("Criação realizada com sucesso")
                time.sleep(1)
                st.rerun()

        else: st.write("Não existe outro usuario no sistema para ser adicionado")
            
    def EditarContato():
        st.header("Editar contato")
        if (len(Servico.ListarMeusContato(st.session_state["user_id"])) > 0):
            c = st.selectbox("Escolha um contato para editar", Servico.ListarMeusContato(st.session_state["user_id"]))
            nome = st.text_input("Digite o nome do contato", c.GetNome())
            if st.button("Atualizar"):
                co = Contato(c.GetId(), c.GetIdUsuarioContato(), c.GetIdUsuario(), nome)
                Servico.EditarContato(co)
                st.success("Atualização realizada com sucesso")
                time.sleep(1)
                st.rerun()
        else: st.write("Você não possui contatos registrados")

    def ExcluirContato():
        st.header("Excluir contato")
        if (len(Servico.ListarMeusContato(st.session_state["user_id"])) > 0):
            c = st.selectbox("Escolha um contato para excluir", Servico.ListarMeusContato(st.session_state["user_id"]))
            if st.button("Excluir"):
                Servico.ExcluirContato(c)
                st.success("Exclusão realizada com sucesso")
                time.sleep(1)
                st.rerun()
        else: st.write("Você não possui contatos registrados")




    
    def Grupos():
        st.title("Meus grupos")
        tab1, tab2, tab3, tab4, tab5,tab6, tab7, tab8 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Sair de um grupo", "Ver um grupo", "Adicionar Membros", "Promover/Rebaixar Membro"])
        with tab1: UsuarioUI.ListarGrupos()
        with tab2: UsuarioUI.CriarGrupo()
        with tab3: UsuarioUI.EditarGrupo()
        with tab4: UsuarioUI.ExcluirGrupo()    
        with tab5: UsuarioUI.Sair()  
        with tab6: UsuarioUI.VerGrupo()  
        with tab7: UsuarioUI.AdicionarMembro() 
        with tab8: UsuarioUI.PromoverMembro() 
    
    def ListarGrupos():
        st.header("Listagem de grupos")

        if (len(Servico.ListarGruposQueCriei(st.session_state["user_id"])) > 0):
            df = pd.DataFrame(Servico.ListarGruposQueCriei(st.session_state["user_id"]))
            st.table(df)
        else:
            st.write("Você não criou nenhum grupo")

        if (len(Servico.ListarGruposQueParticipo(st.session_state["user_id"])) > 0):
            df = pd.DataFrame(Servico.ListarGruposQueParticipo(st.session_state["user_id"]))
            st.table(df)
        else:
            st.write("Você não foi inserido em nenhum grupo")

    def CriarGrupo():
        st.header("Criação de Grupo")
        nome = st.text_input("Digite um nome:")
        desc = st.text_input("Digite uma descrição:")
        if st.button("Criar"):
            g = Grupo(0,nome,desc,st.session_state["user_id"])
            Servico.InserirGrupo(g)
            st.success("Criação realizada com sucesso")
            time.sleep(1)
            st.rerun()

    def EditarGrupo():
        st.header("Edição de grupo")
        if (len(Servico.ListarGruposQueCriei(st.session_state["user_id"])) > 0):
            g = st.selectbox("Escolha um grupo para editar", Servico.ListarGruposQueCriei(st.session_state["user_id"]))
            nome = st.text_input("Digite um nome:", g.GetNome())
            desc = st.text_input("Digite uma descrição:", g.GetDesc())
            if st.button("Atualizar"):
                gp = Grupo(g.GetId(), nome, desc, g.GetIdCriador())
                Servico.EditarGrupo(gp)
                st.success("Atualização realizada com sucesso")
                time.sleep(1)
                st.rerun()

    def ExcluirGrupo():
        st.header("Exclusão de grupo")
        if (len(Servico.ListarGruposQueCriei(st.session_state["user_id"])) > 0):
            g = st.selectbox("Escolha um grupo para apagar", Servico.ListarGruposQueCriei(st.session_state["user_id"]))
            if st.button("Exluir"):
                Servico.ExcluirGrupo(g)
                st.success("Criação realizada com sucesso")
                time.sleep(1)
                st.rerun()
        else:
            st.write("sem grupos cadastrados")
            
    

    def VerGrupo():
        st.header("Ver um grupo")
        if (len(Servico.ListarGruposAssociados(st.session_state["user_id"])) > 0):
            g = st.selectbox("Escolha um grupo para visualizar", Servico.ListarGruposAssociados(st.session_state["user_id"]))
            st.write(g.GetNome())
            st.write("Descrição: " + g.GetDesc())
            st.write("Membros")
            st.table(pd.DataFrame(Servico.ListarMembrosDoGrupo(g.GetId(), st.session_state["user_id"])))
        else: 
            st.write("Você não criou nenhum grupo")

    def AdicionarMembro():
        st.header("Adicionar membro")
        adicionar = True
        if (len(Servico.ListarGruposQueCriei(st.session_state["user_id"])) > 0):
            g = st.selectbox("Escolha um grupo para adicionar um membro", Servico.ListarGruposQueCriei(st.session_state["user_id"]))
        else: 
            st.write("Você não criou nenhum grupo")
            adicionar = False
        if (len(Servico.ListarMeusContato(st.session_state["user_id"])) > 0):
            c = st.selectbox("Escolha um contato para ser adicionado", Servico.ListarMeusContato(st.session_state["user_id"]))
        else: 
            st.write("Você não possui contatos")
            adicionar = False
        if adicionar == True:
            if st.button("Adicionar membro"):
                m = Membro(0, g.GetId(), c.GetIdUsuarioContato(), False)
                Servico.AdicionarMembro(m)
                st.success("Sucesso ao adicionar membro")
                time.sleep(1)
                st.rerun()
    def PromoverMembro():
        st.header("Promover/Rebaixar Membro")
        g = st.selectbox("Selecione um grupo para promover ou rebaixar", Servico.GruposQueSouAdmOuCriador(st.session_state["user_id"]))
        ms = st.selectbox("Selecione o membro do grupo para promover ou rebaixar", Servico.MembrosGerenciaveis(g.GetId(), st.session_state["user_id"]))
        if ms is not None:
            adm = st.checkbox("Adm", ms.GetSenha())

        if st.button("Atualizar membro") and ms is not None:
            Servico.PromoverMembro(g.GetId(), ms.GetId(), adm)
            st.success("Sucesso ao atualizar membro")
            time.sleep(1)
            st.rerun()
        
    def Sair():
        st.header("Sair de um grupo")
        if (len(Servico.ListarGruposQueParticipo(st.session_state["user_id"])) > 0):
            g = st.selectbox("Selecione um grupo para sair", Servico.ListarGruposQueParticipo(st.session_state["user_id"]))
            if st.button("Sair do grupo"):
                m = Membro(0, g.GetId(),st.session_state["user_id"], False )
                Servico.ExcluirMembro(m)
                st.success("Saida realizada com sucesso")
                time.sleep(1)
                st.rerun()
        else:
            st.write("Você não foi inserido em nenhum grupo")

    
