N = int(input('Digite um numero inteiro: '))
L = []
try: 
    for i in range(N):

        X = float(input(f'Elementos {i}: '))
        L.append(X)
    print('\nResultado')

    for valor in L:
        print(f'{valor:.2f}')

except ValueError:
    print('Só numero reais')
  