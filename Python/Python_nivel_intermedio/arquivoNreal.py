arq = open('numero.txt', 'w')
A = float(input('Digite os números: '))
while A != 0:
    arq.write(f'{A:.3f} \n')
    A = float(input('Digite os números: '))
arq.close()
print('Fim do programa--->')