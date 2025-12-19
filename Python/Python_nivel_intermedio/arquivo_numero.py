arq = open('numero3.txt', 'w')
B = float(input('Digite a sequencia: '))
while B != 0:
    arq.write(f'{B:.2f} \n')
    B = float(input('Digite a sequencia: '))
arq.close()
print('Fim do programa->>>')