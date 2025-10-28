# Este programa embora funcione correctamente, não é pythonico
P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razação: '))
Q = int(input('Digite a quantidade de termos: '))
Termos = [P]
i=0

while i <= Q - 1 :
    P = P+R
    Termos.append(P)
    i+=1
print('Lista resultante')
print(Termos)
print('Fim do programa')
