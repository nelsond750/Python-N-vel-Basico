"""
Exercício Proposto 10.3
Enunciado:

Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos: nome, número celular, email e data de aniversário.
A chave deve ser o nome. O valor deve ser uma tupla contendo os demais dados.
Se o nome já existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.
Ao digitar um string vazio para o nome, o programa interrompe a leitura. Antes de encerrar o programa apresente os dados em um formato de tabela.
"""
dicContacto = {}
while True:
    nome = input('Digite nome: ')
    if nome == '':
        break
    
    telefone = input('Digite o numero de telefone: ')
    email = input('Digite o email: ')
    data = input('Data aniversario: ')
    dicContacto[nome] = (telefone, email, data)

