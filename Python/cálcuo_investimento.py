print('Inicio do programa')

investimento = float(input('Digite o investimento: '))
custo = float(input('Digite o custo: '))
receita = float(input('Digita o valor da receita'))
Roi = ((receita - (custo+investimento))*100/(custo+investimento))
print(f'Roi = {Roi:.1f}%')

print('Fim programa')