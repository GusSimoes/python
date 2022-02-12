#estrututas.py

#Estruturas de decisão
"""
temp=int(input('Entre com a temperatura atual:'))

if temp <0:
    print('Congelado')
elif temp <20:
    print('Frio')
elif temp<25:
    print('Normal')
elif temp<35:
    print ('Quente')
else:
    print('Muito quente')

print('Exemplo loop while')
num=1
while(num<10):
    num += 1
    if(num==4):
      continue
    print(num)
    if (num ==7):
        break

print('\nExemplo loop for')
for x in range(10):
    print(x)
    if(num==4):
        continue
    print(x)
    if (x==7):
        break
"""
print('Alfabeto')
for c in range(65,91):
    print(chr(c)+ chr(c+32),end='')
