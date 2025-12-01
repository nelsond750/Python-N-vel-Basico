"""
Exercício Proposto 7.13
Enunciado: 

Escreva um programa que permaneça em laço lendo três dados de um produto: o código (int), o preço de compra (float) e o preço de venda(float). 
Com esses dados forme uma tupla e armazene-a em uma lista. Os três dados devem ser lidos em uma única linha separados por espaço em branco.
O laço termina quando forem digitados três zeros: 0 0 0
Em seguida, para todas as tuplas presentes na lista, exiba o código do produto e a margem bruta de lucro do produto em porcentagem e com uma casa decimal.
A margem bruta de lucro é calculada com a expressão:
𝑀𝑎𝑟𝑔𝑒𝑚𝐵𝑟𝑢𝑡𝑎=( 𝑃𝑟𝑒ç𝑜 𝑉𝑒𝑛𝑑𝑎/𝑃𝑟𝑒ç𝑜 𝑑𝑒 𝐶𝑜𝑚𝑝𝑡𝑎−1 ).100%
"""




produtos = []
while True:
    
    T = input('Digite os dados do produto (ou 0 0 0 para sair): ')
    if T  == '0 0 0':
        print('Fim do programa.')
        break
   
    codigo, preco_compra,preco_venda = T.split()
    codigo=int(codigo)
    preco_compra=float(preco_compra)
    preco_venda=float(preco_venda)
    Tupla = (codigo,preco_compra,preco_venda)
    produtos.append(Tupla)
for codigo,preco_compra,preco_venda in produtos:
    MargemBruta = (preco_venda/preco_compra -1 )*100
    print(f'Produto: {codigo} possui a margem bruta = {MargemBruta:.1f}% ')