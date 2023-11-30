import json
from Jogo import Jogo

#Classe que involve a persistencia do Jogo
class NJogo:
    __Jogos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0  # encontrar o maior id já usado
        for aux in cls.__Jogos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__Jogos.append(obj)  # insere um jogo (obj) na lista
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.__Jogos  # retorna a lista de jogos

    @classmethod
    def AcharPorId(cls, id):
        cls.Abrir()
        for obj in cls.__Jogos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.get_id())
        if aux is not None:
            aux.set_nome(obj.get_nome())
            aux.set_descricao(obj.get_descricao())
            aux.set_preco(obj.get_preco())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.get_id())
        if aux is not None:
            cls.__Jogos.remove(aux)
        cls.Salvar()
        
    @classmethod
    def Abrir(cls):
        cls.__Jogos = []
        try:
            with open("jogos.json", mode="r") as arquivo:
                jogos_json = json.load(arquivo)
                for obj in jogos_json:
                    aux = Jogo(obj["id"], obj["nome"], obj["descricao"], obj["preco"])
                    cls.__Jogos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("jogos.json", mode="w") as arquivo:
            json.dump(cls.__Jogos, arquivo, default=Jogo.to_json)
        #mode w = write, r = read
