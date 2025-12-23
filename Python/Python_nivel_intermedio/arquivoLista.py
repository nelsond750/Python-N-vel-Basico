Lst = []

A = float(input('Digite um real: '))
while A != 0:
    Lst.append(f'{A:.3f} \n')
    A = float(input('Digite um real: '))
arq = open('saida_er_11.txt', 'w')
arq.writelines(Lst)
arq.close()
print('Fim do programa->>>')