arq = open('saida_er_11.txt', 'w')
A = int(input('Digite um inteiro: '))

while A != 0:
    arq.write(f'{A} \n')
    A = int(input('Digte um inteiro: '))
arq.close()
print('Fim do programa->>>')