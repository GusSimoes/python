class Produto:
    #construtor da classe, passa os parametros para criar o produto
    def __init__(self, descricao, preco, quantidade, id):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade


    #funções para ler as variáveis privadas = getter (pegar)
    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def id(self):
        return self.__id

    #funções para alterar as variáveis privadas = setter (setar)
    @descricao.setter
    def descricao(self,descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        return f'Código: {self.id} \tDescrição: {self.descricao} \tPreço: R$ {self.preco} \tQuantidade : {self.quantidade}'


