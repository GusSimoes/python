#arquivo_txt.py

import sys

#modo de abertura de arquivos:
#'r' = read only (modo leitura)
#'w' = write (modo escrita)
#'a' = append(modo anexar)

lista=[]

def entrada():
    fruta=input('Nome da fruta para adicionar:')
    lista.append(fruta)
    print(fruta + 'adicionar na lista')

def mostrar():
    print('lista=',lista)

def gravar():
    arquivo = open('frutas.txt','w')  #modo escrita
    for fruta in lista:
        arquivo.write(fruta + '\n')

    arquivo.close()
    print('Dados gravados com sucesso')

def ler():
    pass

def anexar():
    pass

def menu():
    print('\n\n######################')
    print('## Controle de listas ##')
    print('1 = entrada de dados')
    print('2 = mostrar dados')
    print('3 = gravar dados')
    print('4 = ler dados')
    print('5 = anexar dados')
    opcao=int(input('Qual opção?'))

    if(opcao==1):
        entrada()
    elif(opcao==2):
        mostrar()
    elif(opcao==3):
        gravar()
    elif(opcao==4):
        ler()
    elif(opcao==5):
        anexar()
    else:
        print('Opção inválida!')



if(__name__=='__main__'):
    while True:  #loop infinito
        menu()
          
