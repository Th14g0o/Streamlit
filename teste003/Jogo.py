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
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def get_preco(self): return self.__preco

    #metodos para salvar valores nos atributos encapsulados(privados)
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_preco(self, preco): self.__preco = preco

    #Se não tiver registros dessa classe, seguir esse padrao
    def to_json(self):
        return {
        'id': self.__id,
        'nome': self.__nome,
        'descricao': self.__descricao,
        'preco': self.__preco}
