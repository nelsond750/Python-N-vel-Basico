Msg = 'Digite Valor'
print('Dados do primeiro conjunto')
C1 = set()
X = int(input(Msg))
while X !=0:
    C1.add(X)
    X = int(input(Msg))
print('Dados do segundo conjunto')
C2 = set()
X = int(input(Msg))
while X != 0:
    C2.add(X)
    X = int(input(Msg))
print(f'\nConjunto 1:{C1}')
print(f'\nConjunto 2:{C2}')
print(f'\nUnião')
print(C1 | C2)
print(f'intersecção')
print(C1 & C2)