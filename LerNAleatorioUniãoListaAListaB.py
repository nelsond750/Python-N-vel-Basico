"""
Exercício Proposto 7.14
Enunciado: 

Escreva um programa que leia um número inteiro nA e gere uma lista A com nA valores inteiros aleatórios, não repetidos e situados na faixa [1, 100].
Mostre-a na tela em ordem crescente. Em seguida leia outro inteiro nB e gere a lista B usando as mesmas regras aplicadas à lista A.
Mostre-a na tela também em ordem crescente.
Crie e exiba uma lista contendo a união das listas A e B, sem conter valores repetidos. Mostre a lista resultante e a quantidade de elementos dela.
Exemplo: 
nA = 7 lista A = [8, 12, 29, 35, 44, 64, 81]
nB = 5 lista B = [10, 25, 35, 38, 64]
Saída: União de A e B
[8, 10, 12, 25, 29, 35, 38, 44, 64, 81] contém 10 elementos
"""
from random import randint

nA = int(input('Digite um numero nA: '))
A = []
for i in range(nA):
    a = randint(1,100)
    if a not in A:
        A.append(a)
        A.sort()
print(f'\n Lista A = {A}')
nB = int(input('Digite um numero nB: '))
B = []

for i in range(nB):
    a = randint(1,100)
    if a not in B:
        B.append(a)
        B.sort()
print(f'\n\n Lista B = {B}')
ResultAB = []
setA = set(A)
setB = set(B)
ResultAB= list(setA|setB)
ResultR = (list(A+B))
print(f'Resultante {ResultAB} contém {len(ResultAB)} elementos')

        