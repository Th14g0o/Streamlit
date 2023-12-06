import json

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def GetId(self):
        return self.__id
    def GetNome(self):
        return self.__nome
    def GetEmail(self):
        return self.__email
    def GetSenha(self):
        return self.__senha

    def SetId(self, i):
        self.__id = i
    def SetNome(self, n):
        self.__nome = n
    def SetEmail(self, e):
        self.__email = e
    def SetSenha(self, s):
        self.__senha = s

    def __str__(self):
        return f"{self.__nome} | {self.__email} | {self.__senha}"

    def ToJson(self):
        return {
        'id': self.__id, 
        'nome': self.__nome,
        'email': self.__email,
        'senha': self.__senha}


class NUsuario:
    __Usuarios = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0  
        for aux in cls.__Usuarios:
            if aux.GetId() > id: id = aux.GetId()
        obj.SetId(id + 1)
        cls.__Usuarios.append(obj)  
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.__Usuarios  

    @classmethod
    def AcharPorId(cls, id):
        cls.Abrir()
        for obj in cls.__Usuarios:
            if obj.GetId() == id: 
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            aux.SetNome(obj.GetNome())
            aux.SetSenha(obj.GetSenha())
            aux.SetEmail(obj.GetEmail())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj):
        cls.Abrir()
        aux = cls.AcharPorId(obj.GetId())
        if aux is not None:
            cls.__Usuarios.remove(aux)
        cls.Salvar()

    @classmethod
    def Abrir(cls):
        cls.__Usuarios = []
        try:
            with open("users.json", mode="r") as arquivo:
                usuarios_json = json.load(arquivo)
                for obj in usuarios_json:
                    aux = Usuario(obj["id"], obj["nome"], obj["email"], obj["senha"])
                    cls.__Usuarios.append(aux)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("users.json", mode="w") as arquivo:
            json.dump(cls.__Usuarios, arquivo, default=Usuario.ToJson)
    