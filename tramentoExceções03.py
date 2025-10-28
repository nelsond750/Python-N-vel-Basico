# Tramento de excepção  nomeados e não nomeados
try:

    A = int(input('Digite o primeiro valor: '))
    B = int(input('Digite o segundo valor:  '))
    R = A/B
    print(f' O resultado é: {R}')
except ZeroDivisionError:
    print('O Segundo valor não pode ser zero')

except ValueError:
    print('Digite números inteiro para o primeiro valor e o segundo valor')
except:
    print('Não é possível calcular a divisão')
    


