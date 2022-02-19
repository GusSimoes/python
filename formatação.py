#formatação.py

valor1 = 10
valor2 = 20.9
#pirmeira forma de formatação usando %
print("v1 =%d V2 = R$ %.2f" % (valor1,valor2))

#segunda forma de formatação usando {}
print("v1=R$ {} v2 = R$ {:.2f}".format(valor1,valor2))

print("Olá Sr.{0}{1}".format("Joao","Ferreira"))
print("Sobrenome:{1}\tNome{0}".format("Joao","Ferreira"))

print("R${:6.1f}".format(1000.12)) #total de 6 posições sendo 1 decimal
print("R${:07.2f}".format(4.11)) #total de 7 posições sendo 2 decimais 

#terceira forma de formatação: f-string
      #a partir da ver~sao 3.6 do python foi incluido o recusro chamado : f-string

nome="Matheus"
print(f'Meu nome é {nome}')

print(f'Meu nome é {nome.lower()}')

