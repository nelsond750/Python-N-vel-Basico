X = 1
totalPar = 0
totalImpar = 0
while X != 0:
    X = int(input('Digite o numero: '))
    if X % 2 == 0:
        totalPar = totalPar+1
        print(f'{X} é Par   ')
    else:
        print(f'{X} é impar')
        totalImpar = totalImpar+1

print(f'Quantidade de par digitado é :{totalPar} \n Quantidade Impar digitado é: {totalImpar}')
