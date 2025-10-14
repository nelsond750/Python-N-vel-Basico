LMin = int(input('Digite o limite mínimo: '))
LMax = int(input('Digite o limite máximo: '))
if LMin > LMax:
    print('Limite mínimo maior que o máximo.')
else:
    cont = LMin
while cont <= LMax:
    print(cont)
    cont+=1
    