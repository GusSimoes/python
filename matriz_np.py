#matriz_np.py

#matriz com numpy

#para instalar uma biblioteca do python entrar
#em C:\Users\ALUNO-401\AppData\Local\Programs\Python\Python310\Scripts
#pip install numpy


import numpy as np

print("Matriz usando numpy...")
matriz = np.array([
                    [1,2,5,6],
                    [3,4,8,9],
                    [3,4,8,9],
                    [1,2,5,6]
                 ])

print(matriz)
print('Matriz[3,3] = ', matriz[3][3])
