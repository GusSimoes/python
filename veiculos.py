#veiculos.py

#classe mãe
class Veiculo:

    def __init__(self,marca,modelo,placa,ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def __str__ (self):
        return 'Veiculo placa:' + self.placa

    def ligar(self):
        print('Veiculo ligado...')

    def abastecer(self):
        print('Veiculo abastecendo...')

#classe filho
class Carro(Veiculo):
    def __init__(self,marca,modelo,placa,ano,cor):
        super().__init__(marca,modelo,placa,ano) #super chama da classe mãe
        self.cor = cor

    def ligar(self):
        print('Carro ligado')

    def abastecer(self):
        print('Carro abastecendo...')

#classe motocicleta
class Motocicleta(Veiculo):
    def __init__(self,marca,modelo,placa,ano,cilindrada):
        super().__init__(marca,modelo,placa,cilindrada) #super chama da classe mãe
        self.cilindrada = cilindrada

    def ligar(self):
        print('Moto ligada')

    def abastecer(self):
        print('Moto abastecendo...')



