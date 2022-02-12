#espiral.py

import turtle


#           0   1       2       3       4       5           6       7       8       9
cores = ['red','yellow','blue','green','orange','purple','white','brown','gray','pink'] #10cores
turtle.bgcolor("black")
turtle.speed(100)

def linhas():
    lados=turtle.numinput('Escolha entre 2 e 6','Número de lados:')


    for x in range(50):
        indice = x % 6 #0..5
        turtle.pencolor(cores[indice])
        turtle.forward(x * 5)
        turtle.left(360/(lados+1))
        turtle.width(x*lados/10)


def roseta():
    numero=int(turtle.numinput('Número de círculos','Quantos círculos você quer?:',6))
    t=turtle.Pen()
    t.speed(10000)
    
    t.pencolor('yellow')
    for x in range(numero):
        t.circle(100)
        t.left(360/numero)

    t.pencolor('purple')
    for x in range(numero):
        t.circle(300)
        t.left(360/numero)        


def animais():
    t=turtle.Pen()
    animais=[] #lista vazia
    nome = turtle.textinput('Nomes de animais:', 'Digite um nome ou ENTER para terminar:')

    #continua pedindo nomes
    while nome !="" and len(animais) < len(cores):
        #Adiciona o nome à lista de aniamis
        animais.append(nome.title())
        #Pede outro nome ou termina
        nome=turtle.textinput('Nomes de animais','Digite um nome ou Enter para terminar:')

    #Desenha espiral com os nomes dos animais
    for x in range(100):
        t.pencolor(cores[x%len(animais)]) #circula pelas cores
        t.penup()                        #não desenha as linahs normais da espiral
        t.forward(x*4)                   #apenas move a tartaruga pela tela sem desenhar
        t.pendown()                      #desenha nome do próximo animal
        t.write(animais[x%len(animais)],font=('Arial', int((x+4)/4),"bold"))
        t.left(360/len(animais)+2)
    

if(__name__=='__main__'):
    #roseta()
    animais()
