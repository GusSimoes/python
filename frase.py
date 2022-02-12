#calc_exp.py


expressao = input("Digite uma expressao:")
print(expressao)

lista = expressao.split('+')
print(lista)

soma = 0
for x in lista:
    soma=soma+int(x)

print('Soma:',soma)
