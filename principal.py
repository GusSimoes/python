#principal.py

from veiculos import *

def principal():

    veiculo = Veiculo('Marca','modelo','AAA-0090',1)

    carro = Carro ('VW','Polo','ABC-1234',2000,'Branco')
    moto = Motocicleta('Harley','Fat Boy','AXX-1333',2021,800)

    veiculo.abastecer()
    #chama __str__ automaticamente
    print(veiculo)

    lista = [veiculo,carro,moto,'banana',123,3.14]

    for item in lista:
        if (isinstance (item,Carro)):
            print('Temos um carro na lista')
        elif (isinstance (item,Motocicleta)):
            print('Temos uma motocicleta na lista')
        elif (isinstance (item,Veiculo)):
            print('Temos um veiculo na lista')
        elif (isinstance (item,str)):
            print('Temos uma string na lista')
        elif (isinstance (item,int)):
            print('Temos um int na lista')
        else:
            print('Valor desconhecido na lista')
            

if __name__=='__main__':
    principal()

