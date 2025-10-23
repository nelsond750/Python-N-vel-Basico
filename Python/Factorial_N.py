#Factorial de um número
N = int(input('Digite um numero para saber qual o seu fatorial: '))

factorial = 1
i = N

if N < 0:

    print('Não exite factorial de números negativos ')

else:

    while i > 1:
      factorial *= i
      i -=1 
    print(factorial)
    