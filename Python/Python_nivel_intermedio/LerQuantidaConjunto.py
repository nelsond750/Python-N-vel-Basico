from random import randint

Qtde = int(input('Digite a quantidade: '))
conjunto = set()
for i in range(Qtde):
    a = randint(1,50)
    conjunto.add(a)
    
print(conjunto)