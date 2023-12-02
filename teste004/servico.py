from modelos.usuario import Usuario, NUsuario
from modelos.jogo import Jogo, NJogo

class Servico:

    def IniciarAdm():
        for user in Servico.ListarUsuarios():
            if user.GetNome() == "admin": 
                return
        Servico.CriarUsuario("000", "admin", "admin@gmail.com", "admin") 

    def LogarUsuario(email, senha):
        for user in Servico.ListarUsuarios():
            if user.GetEmail() == email and user.GetSenha() == senha:
                return user
        return None

    
    def ListarUsuarios():
        return NUsuario.Listar()

    def AcharUsuario(id):
        return NUsuario.AcharPorId(id)

    def RemoverUsuario(id, nome, email, senha):
        user = Usuario(id,nome,email,senha)
        return NUsuario.Excluir(user)

    def CriarUsuario(id, nome, email, senha):
        user = Usuario(id,nome,email,senha)
        return NUsuario.Inserir(user)

    def EditarUsuario(id, nome, email, senha):
        user = Usuario(id,nome,email,senha)
        return NUsuario.Atualizar(user)

    
    
    def ListarJogos():
        return NJogo.Listar()

    def AcharJogo(id):
        return NJogo.AcharPorId(id)

    def RemoverJogo(j):
        return NJogo.Excluir(j)

    def CriarJogo(id, nome, descricao, valor):
        user = Jogo(id,nome,descricao,valor)
        return NJogo.Inserir(user)

    def EditarJogo(id, nome, descricao, valor):
        user = Jogo(id,nome,descricao,valor)
        return NJogo.Atualizar(user)