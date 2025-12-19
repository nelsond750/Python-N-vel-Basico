"""
Exercício Resolvido 11.5

Enunciado: Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo tem um número inteiro em cada linha. 
Todos os números lidos devem ser mostrados na tela.
Mostrar também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor. 
Usar aqui o mesmo arquivo de entrada do exercício anterior.

Usar um iterador for e o arquivo como iterável.
"""

Lst = []

for linha in open('saida_er_11.txt'):
    Lst.append(int(linha))
print('Valores lidos do arquivos')
print(Lst)
soma = sum(Lst)
print(f'Soma dos valore {soma}')
qtde = len(Lst)
print(f'A quantidade dos número: {qtde}')
print(f'Médio dos valores = {soma/qtde}')
Minimo = min(Lst)
print(f'Minimo dos valore {Minimo}')
Max = max(Lst)
print(f'Máxima dos valores {Max}')
print('Fim do programa->>>')