#Usando while-else

X = 1
while X > 0:
    X = int(input('Digite um numero'))
    if X == 0:
        print('Você digitou zero')
        break
    print(X)
else:
    print('Você digitou negativo...')
    
print('Fim do Programa')
