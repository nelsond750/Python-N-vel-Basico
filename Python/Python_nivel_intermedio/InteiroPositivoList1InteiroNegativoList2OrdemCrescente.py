N = int(input('Digite um numero: '))
LPos = []
LNeg = []

for i in range(N):
    X = int(input(f'Elemento {i}: '))
    if X < 0:
        LNeg.append(X)
        LNeg.sort()
    else:
        LPos.append(X)
        LPos.sort()
        
print(f'Valores positivos: {LPos}, contém: {len(LPos)}')
print(f'Valores positivos: {LNeg}, contém: {len(LNeg)}')

