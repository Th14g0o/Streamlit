import json
class Membro:
    def __init__(self, id, idGrupo, idUsuario, adm):
        self.__id = id
        self.__idGrupo = idGrupo
        self.__idUsuario = idUsuario
        self.__adm = adm

    def GetId(self): return self.__id
    def GetAdm(self): return self.__adm
    def GetIdUsuario(self): return self.__idUsuario
    def GetIdGrupo(self): return self.__idGrupo

    def SetId(self, valor):  self.__id = valor
    def SetAdm(self, valor):  self.__adm = valor
    def SetIdUsuario(self, valor):  self.__idUsuario = valor
    def SetIdGrupo(self, valor):  self.__idGrupo = valor

    def ToJson(self):
        return{
           'id' : self.__id,
           'adm' : self.__adm,
           'idGrupo' : self.__idGrupo,
           'idUsuario' : self.__idUsuario
        }
        
    def __str__(self):
        return f"{self.__id} - {self.__idGrupo} - {self.__idUsuario} - {self.__adm}"



class NMembro:
    __Membros = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0  
        for aux in cls.__Membros:
            if aux.GetId() > id: 
                id = aux.GetId()
        obj.SetId(id + 1)
        cls.__Membros.append(obj)  
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.__Membros 

    @classmethod
    def AcharPorId(cls, id):
        cls.Abrir()
        for obj in cls.__Membros:
            if obj.GetId() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            aux.SetAdm(obj.GetAdm())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            cls.__Membros.remove(aux)
        cls.Salvar()
        
    @classmethod
    def Abrir(cls):
        cls.__Membros = []
        try:
            with open("membros.json", mode="r") as arquivo:
                membroJson = json.load(arquivo)
                for obj in membroJson:
                    aux = Membro(obj["id"], obj["idGrupo"], obj["idUsuario"], obj["adm"])
                    cls.__Membros.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("membros.json", mode="w") as arquivo:
            json.dump(cls.__Membros, arquivo, default=Membro.ToJson)
  
