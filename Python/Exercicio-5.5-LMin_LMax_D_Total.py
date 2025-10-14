LMin = int(input('Digite um numero: '))
LMax = int(input('Digite outro numero: '))
if LMin > LMax:
    print('Limite mínimo maior que o máximo.')
else:
    D = int(input('Digite o valor que pretende saber o divor: '))
    cont = LMin
    total =0
    while cont <= LMax:
        if cont % D == 0:
            total +=1
            print(cont)
           
        cont+=1
print(f'total de números divisíveis por {D}: {total}')
