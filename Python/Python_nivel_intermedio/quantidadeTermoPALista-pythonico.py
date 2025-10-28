P = int(input('Digite o primeiro termo (P): '))
R = int(input('Digite a razação (R): '))
Q = int(input('Digite a quantidade (Q): '))

pa = []
i = 0

while i < Q :
    
    termos = P+i*R
    pa.append(termos)
    i+=1 
# A impressão dos termos   
print(pa)
    