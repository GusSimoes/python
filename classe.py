#conta.py

class Conta:
    #propriedades
    #funções builtin
    def __init__(self,numero,titular,saldo,limite):
        print("Inicializando o objeto:{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #métodos
    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        if self.__saldo+self.__limite >= valor:
            self.__saldo -= valor
            return True
        else:
            print('Não há saldo para sacar')
            False
            
    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod  #método estático é aquele compartilhado entre todos os objetos
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return{'BB':'001','Caixa':'104','Bradesco':'237'}
    
    
#contaJoao = Conta(123,'Joao da Silva',50,1000)
#contaZe = Conta(456,"Jose da Silva",0,580)
#print('Saldo do Zé',contaZe.saldo)

#contaJoao.transferir(50,contaZe)
#print('Limite',contaZe.limite)

#contaZe.limite = 2000
#print('Limite:', contaZe.limite)

print('Codigo do banco',Conta.codigo_banco())
print('Codigo da caixa',Conta.codigos_bancos()['Caixa'])
