import json

class Grupo:
    def __init__(self,id, nome, desc, idCriador):
        self.__id = id
        self.__nome = nome
        self.__desc = desc
        self.__idCriador = idCriador

    def GetId(self): return self.__id
    def GetNome(self): return self.__nome
    def GetDesc(self): return self.__desc
    def GetIdCriador(self): return self.__idCriador

    def SetId(self, valor):  self.__id = valor
    def SetNome(self, valor):  self.__nome = valor
    def SetDesc(self, valor):  self.__desc = valor
    def SetIdCriador(self, valor):  self.__idCriador = valor

    def __str__(self): return f"{self.__nome}({self.__id}) | {self.__desc}"

    def ToJson(self):
        return{
           'id' : self.__id,
           'nome' : self.__nome,
           'desc' : self.__desc,
           'idCriador' : self.__idCriador
        }


class NGrupo:
    __Grupos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0  
        for aux in cls.__Grupos:
            if aux.GetId() > id: 
                id = aux.GetId()
        obj.SetId(id + 1)
        cls.__Grupos.append(obj)  
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.__Grupos 

    

    @classmethod
    def AcharPorId(cls, id):
        cls.Abrir()
        for obj in cls.__Grupos:
            if obj.GetId() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            aux.SetNome(obj.GetNome())
            aux.SetDesc(obj.GetDesc())
            aux.SetIdCriador(obj.GetIdCriador())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            cls.__Grupos.remove(aux)
        cls.Salvar()
        
    @classmethod
    def Abrir(cls):
        cls.__Grupos = []
        try:
            with open("grupos.json", mode="r") as arquivo:
                gruposJson = json.load(arquivo)
                for obj in gruposJson:
                    aux = Grupo(obj["id"], obj["nome"], obj["desc"], obj["idCriador"])
                    cls.__Grupos.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("grupos.json", mode="w") as arquivo:
            json.dump(cls.__Grupos, arquivo, default=Grupo.ToJson)
  
