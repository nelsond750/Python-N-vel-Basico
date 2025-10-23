n = -1

while n != 0:

    n = int(input('Digite um numero inteiro: '))

    match n:
        case 1:
            print('Você Digitou um')
        case 2:
            print('Você Digitou dois')
        case 3:
            print('Você Digitou três')
        case 4:
            print('Você Digitou quatro')
        case _:
            print('Você Digitou outra coisa')

print('\n\n Fim do programa')