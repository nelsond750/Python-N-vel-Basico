from random import randint
Lst = []
Qtde = int(input('Digite a quantidade: '))
for i in range(Qtde):
    a = randint(1, 100)
    Lst.append(a)
print('\n Antes de eliminar repetição')
print(f'{Lst}')
X = 1
while X > 0:
    X = int(input('Digite um valor '))
    if X in Lst:
        while X in Lst:
                Lst.remove(X)
        print(f'{Lst}\n E a quantidade após a remoção é:{Lst.count(X) }')
        
    else:
        print(f'\n O número {X} não está na lista. Fim do programa.')
        break