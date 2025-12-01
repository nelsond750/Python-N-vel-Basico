"""
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade de inteiros aleatórios.
Exiba a lista na tela. Em seguida elimine valores que estiverem repetidos, deixando apenas uma ocorrência de cada. 
Exiba a nova lista sem repetidos e o seu tamanho.
"""
from random import randint

Qtde = int(input('Digite a quantidade '))
Lst =  []

for i in range(Qtde):
    Lst.append(randint(1,100))
print(f'\nLista gerada:')
print(Lst)
conjunto = set(Lst)
Lst = set(conjunto)
print('\Lista com valores não repetidos: ')
print(Lst)
print(f'A nova lista tem {len(Lst)} elementos')