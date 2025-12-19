estoque = {}
for linha in open('Entrada_dic.txt'):
    lst = linha.rstrip().split(';')
    cod = int(lst[0])
    qtde =int(lst[1])
    pcunit = float(lst[2])
    estoque[cod] = (qtde, pcunit)
print('Valores carregados no dicionario')
print(estoque)
print('\n Exibição dos dados na forma de tababela')
totalGeral = 0
for cod, dados in estoque.items():
    tot = dados[0]*dados[1]
    totalGeral +=tot
    print(f'{cod}: {dados[0]:5d} X {dados[1]}')
print(''*24,f'totalGeral:8.2f')
print('\nFim do programa')