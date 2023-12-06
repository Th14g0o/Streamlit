import json

class Contato:
    def __init__(self, id, idUsuarioContato, IdUsuario, nome):
        self.__id = id
        self.__idUsuarioContato = idUsuarioContato
        self.__IdUsuario = IdUsuario
        self.__nome = nome

    def GetId(self): return self.__id
    def GetNome(self): return self.__nome
    def GetIdUsuarioContato(self): return self.__idUsuarioContato
    def GetIdUsuario(self): return self.__IdUsuario

    def SetId(self, valor):  self.__id = valor
    def SetNome(self, valor):  self.__nome = valor
    def SetIdUsuarioContato(self, valor):  self.__idUsuarioContato = valor
    def SetIdUsuario(self, valor):  self.__IdUsuario = valor

    def __str__(self): return f"{self.__nome}({self.__id}) | {self.__idUsuarioContato}"

    def ToJson(self):
        return{
           'id' : self.__id,
           'nome' : self.__nome,
           'IdUsuario' : self.__IdUsuario,
           'idUsuarioContato' : self.__idUsuarioContato
        }




class NContato:
    __Contatos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0  
        for aux in cls.__Contatos:
            if aux.GetId() > id: 
                id = aux.GetId()
        obj.SetId(id + 1)
        cls.__Contatos.append(obj)  
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.__Contatos 


    @classmethod
    def AcharPorId(cls, id):
        cls.Abrir()
        for obj in cls.__Contatos:
            if obj.GetId() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            aux.SetNome(obj.GetNome())
            aux.SetIdUsuarioContato(obj.GetIdUsuarioContato())
            aux.SetIdUsuario(obj.GetIdUsuario())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            cls.__Contatos.remove(aux)
        cls.Salvar()
        
    @classmethod
    def Abrir(cls):
        cls.__Contatos = []
        try:
            with open("contatos.json", mode="r") as arquivo:
                contatoJson = json.load(arquivo)
                for obj in contatoJson:
                    aux = Contato(obj["id"], obj["idUsuarioContato"], obj["IdUsuario"], obj["nome"])
                    cls.__Contatos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("contatos.json", mode="w") as arquivo:
            json.dump(cls.__Contatos, arquivo, default=Contato.ToJson)
  
