#pip install pywin32

import random
import win32com.client as win32

def jogar():
    speaker=win32.Dispatch('SAPI.SpVoice')
    speaker.Speak('Bem vindo ao jogo de adivinhação, Gustavo')


    print('##########################################')
    print("Bem vindo ao jogo de Adivinhação, Gustavo")
    print('##########################################')

    numero_secreto=random.randrange(1, 101) #gera um numero entre 1 e 100

    pontos = 1000


    print('Qual o nível de dificuldade?')
    print('(1)Fácil (2) Médio (3) Difícil')

    nivel=int(input('Defina o nível:'))

    if (nivel==1):
        total_tentativas = 20
    elif (nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for tentativa in range(1,total_tentativas+1):
        print(f'Tentativa{tentativa} de {total_tentativas}')

        chute = int(input('Digite um número entre 1 e 100: '))
        if(chute < 1 or chute > 100):
            print('Vc deve digitar um número entre 1 e 100:')
            continue

        if(chute == numero_secreto):
            print('Acertou')
            break
        else:
            pontos_perdidos =abs(numero_secreto - chute )   #valor absoluto (sem sinal)
            pontos = pontos - pontos_perdidos
            
            if (chute > numero_secreto):
                print('Errou! Seu chute foi maior que o número secreto')
            else:
                print('Errou! Seu chute foi menor que o número secreto')

    print('FIM DO JOGO')
    speaker.Speak('Fim do jogo')
    print (f'O número secreto era {numero_secreto}. Vc fez {pontos} pontos')            
    speaker.Speak(f'O número secreto era{numero_secreto}.Você fez {pontos} pontos')

#se não importar, executa
if (__name__=='__main__'):
    jogar()
