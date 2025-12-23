num = 10
arq =open('arvore.txt', 'w')

for i in range(num):
    print(' '*(num-i-1), '*'*(2*i-1))

print(f'        | ')
arq.close()