N = int(input('Digite um numero inteiro: '))
L = []
try: 
    for i in range(N):

        X = float(input(f'Elementos {i}: '))
        L.append(X)
        L.sort()
    print('\n Resultado')
    for valor in L:
        print(f'{valor}')
except ValueError:
    print('Só numero reais')
  

