codigos = [103, 117, 121,135,161,185,200,206,204,16]

Lista = []

print('\n Alternativa com If classico: ')
for codigo in codigos:
    if codigo >= 120 and codigo <= 200:
        Lista.append(codigo)
print(f'\n\n Codigo Filtrado {Lista}')

