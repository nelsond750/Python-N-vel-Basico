D = int(input('Digite um numero maior que zero: '))
if D <= 0:
    print(f'O valor de {D} é inválido')
else:
    i = 1
    while i < 100:
        if i % D == 0:
            print(i)
        i = i+1
print('Fim do programa')