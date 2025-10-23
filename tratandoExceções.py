# Aqui tratamos o erro em caso haja alguma divisão por zero, mas um valor que não seja inteiro poderá dar erro.
A = int(input('digite o primeiro valor: '))

B = int(input('Digite o segundo valor: '))

try:
    R = A/B
    print(f'A divisão é: {R}')


except:
    print('Não é possivel calcular a divisão.')