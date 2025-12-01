"""
Exercício Resolvido 10.2
Enunciado: 
        Escreva um programa que leia do teclado o código de um produto e seu preço unitário. 
O código é um string e o preço é real. Acrescente o par código:preço em um dicionário. 
O programa deve verificar se o código já está no dicionário e neste caso deve emitir uma mensagem de erro.
O laço termina quando for fornecido um string vazio para o código. 
Ao final, exibir código e preço, um produto em cada linha.
"""
cadastro = {}

while True:
    codigo = input('Digite o codigo do produto: ')
    if codigo == '':
        print('Fim programa')
        break

    elif:
        preco = float(input('Digite O preço unitário: '))
    if codigo.setdefult() in cadastro:
        print('Erro! Código já cadastrado...')
        
cadastro[codigo]=preco
       
for codigo,preco in cadastro.items():
    print(f'codigo: {codigo} preço: {preco}')