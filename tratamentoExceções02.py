# Tramento de excepção não nomeado/Genérico
try:

    A = int(input('Digite o primeiro valor: '))
    B = int(input('Digite o segundo valor:  '))
    R = A/B
    print(f' O resultado é: {R}')
except:
    print('Não é possível calcular a divisão')
    
