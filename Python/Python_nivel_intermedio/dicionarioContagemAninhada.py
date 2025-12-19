"""
Exercício Proposto 10.4
Enunciado: 
Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos: nome, número celular, email e data de aniversário.
A chave deve ser o nome. O valor deve ser um dicionário aninhado contendo os demais dados.
Se o nome já existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.
Ao digitar um string vazio para o nome, o programa interrompe a leitura. Antes de encerrar o programa apresente os dados em um formato de tabela.
"""

dicContacto = {}

while True:
    nome = input('Digite o nome: ')
    nome = nome.lower()
    if nome == '':
        print('Fim do Programa.')
        break
    email = input('Digite o email: ')
    telefone = input('Digite o telefone: ')
    aniversario =input('Digite o aniversário: ')
    dados_novo= {'email':email, 'telefone':telefone, 'aniversario':aniversario}

    if nome in dicContacto:
        msg =input('Deeseja alterar o nome, s/n ?:')
        print(f'Este nome {nome} já está registado, {msg}')
        if msg == 's' or msg == 'S':
            dicContacto[nome] = dados_novo
        else:
            print('Informações antigas foram mantidas')
    else:
        dicContacto[nome]= dados_novo
        print(f'Novo contacto {nome} registado com sucesso: ')
print('{:16} {:16} {:16} {:>16}'.format('Nome','Email', 'Telefone', 'Aniversario'))
for nome,dados in dicContacto.items():
    print('{:16} {:16} {:16} {:>16}'.format(nome, dados['email'],dados['telefone'],dados['aniversario'])

)