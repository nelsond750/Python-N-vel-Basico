LMin = int(input('Digite um numero: '))
LMax = int(input('Digite outro numero: '))
if LMin > LMax:
    print('Limite mínimo maior que o máximo.')
else:
    D = int(input('Digite o valor que pretende saber o divor: '))
    cont = LMin
    while cont <= LMax:
        if cont % D == 0:
            print(cont)
           
        cont+=1