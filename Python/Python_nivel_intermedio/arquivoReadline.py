"""
Escreva um programa que permaneça que leia um arquivo de entrada, sabendo que esse arquivo tem um número inteiro em cada linha. 
Todos os números lidos devem ser mostrados na tela. 
Mostrar também a soma dos valores, a quantidade, a média aritmética, o menor valor e o maior valor.
Usar um laço while e na leitura usar o método .readline()

"""
Lst = []
arqEntr = open('saida_er_11.txt', 'r')
linha = arqEntr.readline()
while linha != '':
    Lst.append(int(linha))
    linha = arqEntr.readline()
arqEntr.close()
print('Valores lidos do arquivo')
print(Lst)
soma =sum(Lst)
print(f'Soma dos valores = {soma}')
Qtde = len(Lst)
print(f'Quantidade = {Qtde}')
print(f' Média dos valores = {soma/Qtde}')
Minimo = min(Lst)
print(f'Minimo  dos valores = {Minimo}')
Maximo = max(Lst)
print(f'Máximo dos valores = {Maximo}')
print(f'Fim do programa->>')