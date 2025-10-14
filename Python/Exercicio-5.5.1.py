
#Removendo a estrutura if do exercicio 5.5 e manter o programa funcional.
soma=qtde=0
A = int(input('Digite um valor: '))
while A != 0:
    
    A = int(input('Digite um valor: '))
    soma = soma + A
    qtde = qtde + 1
print(f'Soma dos valores = {soma}')
print(f'Quantidade = {qtde}')
