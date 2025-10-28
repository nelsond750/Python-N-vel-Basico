origem = [33,45,10,15,18,100,7,0,9,24, 7%2]
destino1 = origem[3:6]
print(destino1)
destino2 = origem[:]
destino2[2]=12
print(destino2)
print(f'\n {id(destino2)}')
print(f'{4 in (destino2)}')