P = int(input('Digite o promeiro termo: '))
R = int(input('Digite a razação:'))
Q = int(input('Digite a quantidade: '))

ultimo = P + (Q-1)*R
Termos = list(range(P, ultimo +1, R))
print('Lista dos termos')
print(Termos)
print('Fim do programa->')