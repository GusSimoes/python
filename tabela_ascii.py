#tabela_ascii.py

import time

mensagem='um pequeno passo para o python, porém um grande passo para a humanidade!'

"""

for letra in mensagem:
    print(letra,end='')
    time.sleep(0.1)

for i in range(9,0,-1):
    print(i)
    time.sleep(1)
"""

#imprime alfabeto
for c in range(65,91):
    print(chr(c),end='')


#gerador de senha
palavra=input("\nDigite uma palavra:")
print('Senha:', end='')
for letra in palavra:
      print(ord(letra), end='')
