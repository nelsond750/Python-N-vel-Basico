N = int(input('Digite um numero: '))
L1 = []
L2 = []

for i in range(N):
    X = int(input(f'Elemento {i}: '))
    if X < 0:
        L2.append(X)
    else:
        L1.append(X)

print(f'Valores positivos: {L1}, contém: {len(L1)}')
print(f'Valores positivos: {L2}, contém: {len(L2)}')