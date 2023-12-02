import json

#classe modelo
class Jogo:
    #metodo construtor
    def __init__(self, id, nome, descricao, preco):
        #atributo privado = self.__nomeAtributo, publico = self.nomeAtributo
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
    #metodo ToString()
    def __str__(self):
        return f"{self.__nome} - Descrição: {self.__descricao} - Preço: {self.__preco} "
    
    #metodos para pegar valores do atributos encapsulados(privados)
    def GetId(self): 
        return self.__id
    def GetNome(self): 
        return self.__nome
    def GetDesc(self): 
        return self.__descricao
    def GetPrec(self): 
        return self.__preco

    #metodos para salvar valores nos atributos encapsulados(privados)
    def SetId(self, id): 
        self.__id = id
    def SetNome(self, nome): 
        self.__nome = nome
    def SetDesc(self, descricao): 
        self.__descricao = descricao
    def SetPrec(self, preco): 
        self.__preco = preco

    #Se não tiver registros dessa classe, seguir esse padrao
    def to_json(self):
        return {
        'id': self.__id,
        'nome': self.__nome,
        'descricao': self.__descricao,
        'preco': self.__preco}

#Classe que involve a persistencia do Jogo
class NJogo:
    __Jogos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0  # encontrar o maior id já usado
        for aux in cls.__Jogos:
            if aux.GetId() > id: 
                id = aux.GetId()
        obj.SetId(id + 1)
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
            if obj.GetId() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            aux.SetNome(obj.GetNome())
            aux.SetDesc(obj.GetDesc())
            aux.SetPrec(obj.GetPrec())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            cls.__Jogos.remove(aux)
        cls.Salvar()
        
    @classmethod
    def Abrir(cls):
        cls.__Jogos = []
        try:
            with open("games.json", mode="r") as arquivo:
                jogos_json = json.load(arquivo)
                for obj in jogos_json:
                    aux = Jogo(obj["id"], obj["nome"], obj["descricao"], obj["preco"])
                    cls.__Jogos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("games.json", mode="w") as arquivo:
            json.dump(cls.__Jogos, arquivo, default=Jogo.to_json)
        #mode w = write, r = read
