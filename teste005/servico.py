from modelos.usuario import Usuario, NUsuario
from modelos.grupo import Grupo, NGrupo
from modelos.membro import Membro, NMembro
from modelos.contato import Contato, NContato

class Servico:
    def Logar(nome, senha):
        for u in Servico.ListarUsuarios():
            if u.GetEmail() == nome and u.GetSenha() == senha:
                return u
        return None

    def ListarUsuarios():
        return NUsuario.Listar()
    def ListarUsuariosQueNaoAdicioneiComoContato(idUser):
        usuarios = []
        adiciona = True
        for u in Servico.ListarUsuarios():
            for c in Servico.ListarMeusContato(idUser):
                if c.GetIdUsuarioContato() == u.GetId() and c.GetIdUsuario() == idUser:
                    adiciona = False
                    break
            if adiciona == True and u.GetId() != idUser:
                usuarios.append(u)
            adiciona = True
        return usuarios

    def InserirUsuario(u):
        return NUsuario.Inserir(u)
    def EditarUsuario(u):
        return NUsuario.Atualizar(u)
    def ExcluirUsuario(u):
        return NUsuario.Excluir(u)

    def ListarContato():
        return NContato.Listar()
    def InserirContato(c):
        return NContato.Inserir(c)
    def EditarContato(c):
        return NContato.Atualizar(c)
    def ExcluirContato(c):
        return NContato.Excluir(c)

    def ListarMeusContato(idUser):
        Contatos = []
        for c in Servico.ListarContato():
            if c.GetIdUsuario() == idUser:
                Contatos.append(c)
        return Contatos



    def ListarGrupos():
        return NGrupo.Listar()
    def InserirGrupo(g):
        return NGrupo.Inserir(g)
    def EditarGrupo(g):
        return NGrupo.Atualizar(g)
    def ExcluirGrupo(g):
         return NGrupo.Excluir(g)
    def ListarGruposAssociados(idUser):
        grupos = Servico.ListarGruposQueCriei(idUser)
        for g in Servico.ListarGruposQueParticipo(idUser):
            grupos.append(g)
        return grupos

    def ListarGruposQueParticipo(idUser):
        Grupos = []
        for m in NMembro.Listar():
            if m.GetIdUsuario() == idUser:
                g = NGrupo.AcharPorId(m.GetIdGrupo())
                print(m.GetIdUsuario())
                Grupos.append(g) 
        return Grupos
    def ListarGruposQueCriei(idUser):
        Grupos = []
        for g in Servico.ListarGrupos():
            if g.GetIdCriador() == idUser:
                Grupos.append(g) 
        return Grupos

    def AdicionarMembro(m):
        for memb in NMembro.Listar():
            if m.GetIdUsuario() == memb.GetIdUsuario() and m.GetIdGrupo() == memb.GetIdGrupo():
                return None
        else: return NMembro.Inserir(m)

    def ExcluirMembro(m):
        for memb in NMembro.Listar():
            if m.GetIdUsuario() == memb.GetIdUsuario() and m.GetIdGrupo() == memb.GetIdGrupo():
                return NMembro.Excluir(memb)
        else: return None
    def ListarMembrosDoGrupo(idGrp, idUser):
        Membros = []
        g = NGrupo.AcharPorId(idGrp)

        ContatoCriador = False
        for conts in Servico.ListarMeusContato(idUser):
            if conts.GetIdUsuarioContato() == g.GetIdCriador():
                user = NUsuario.AcharPorId(g.GetIdCriador())
                u = Usuario(conts.GetIdUsuarioContato(), conts.GetNome(), user.GetEmail(), "")
                Membros.append(u)
                ContatoCriador = True
        if ContatoCriador == False:
            u = NUsuario.AcharPorId(g.GetIdCriador())
            u.SetSenha("")
            Membros.append(u)

        ContatoMembro = False
        for m in NMembro.Listar():
            if m.GetIdGrupo() == idGrp:
                for c in Servico.ListarMeusContato(idUser):
                    if c.GetIdUsuarioContato() == m.GetIdUsuario():
                        user = NUsuario.AcharPorId(c.GetIdUsuarioContato())
                        u = Usuario(c.GetIdUsuarioContato(), c.GetNome(), user.GetEmail(), m.GetAdm())
                        Membros.append(u)
                        ContatoMembro = True
                        break
                if ContatoMembro == False:
                    u = NUsuario.AcharPorId(m.GetIdUsuario())
                    u.SetSenha(m.GetAdm())
                    Membros.append(u)
                ContatoMembro = False
                    
        return Membros
    def GruposQueSouAdmOuCriador(idUser):
        grupos = []
        grupos = Servico.ListarGruposQueCriei(idUser)
        for m in NMembro.Listar():
            if m.GetAdm() == True and m.GetIdUsuario() == idUser:
                grupos.append(NGrupo.AcharPorId(m.GetIdGrupo()))
        
        return grupos
    def MembrosGerenciaveis(idGrp, idUser):
        membros = []
        g = NGrupo.AcharPorId(idGrp)
        adm = False

        for m in Servico.ListarMembrosDoGrupo(idGrp, idUser):
            if m.GetId() != idUser:
                membros.append(m)
            else:
                if(m.GetSenha() != False):
                    adm = True
            if m.GetId() ==  g.GetIdCriador() and len(membros) > 0:
                membros.pop(0)
           
        if (idUser == g.GetIdCriador()): 
            return membros

        if adm == True:
            index = 0
            for user in membros:
                if user.GetSenha() == True:
                    membros.pop(index)
                index += 1
            return membros

    def PromoverMembro(idGrp, idUser, adm):
        for m in NMembro.Listar():
            m.SetAdm(adm)
            if m.GetIdUsuario() == idUser and m.GetIdGrupo() == idGrp: 
                m.SetAdm(adm)
                return NMembro.Atualizar(m)
        return None
