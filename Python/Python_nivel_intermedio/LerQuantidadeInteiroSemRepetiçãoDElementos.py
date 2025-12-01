"""
Exercício Proposto 7.11

Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade de números inteiros aleatórios quaisquer.
Exiba a lista na tela.Em seguida verifique se existem e elimine valores que estiverem repetidos, deixando apenas uma ocorrência de cada. 
A ordem relativa dos elementos na lista não deve ser alterada, com exceção às consequências da eliminação dos repetidos.
Exiba a nova lista sem repetidos e o seu tamanho. """
from random import randint
Lst = []
Qtde = int(input('Digite a quantidade: '))

# 1. Carrega a lista com números aleatórios
for i in range(Qtde):
    a = randint(1,50)
    Lst.append(a)
print(f'\n Lista inicial: {Lst}')
# 2. Remoção de duplicatas com preservação de ordem
Lst_unica = []
vistos = set() # O Set é usado para rastreamento RÁPIDO
for numero in Lst:
    # Se o número ainda não foi visto...
    if numero not in vistos:
        # 1. Adiciona-o à nova lista (mantendo a ordem)
        Lst_unica.append(numero)
        # 2. Marca-o como visto (para evitar repetição futura)
        vistos.add(numero)
print(f'\n Nova lista: {Lst_unica} tamanho dos elemento: {len(Lst_unica)} ')