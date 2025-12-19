"""
Exercício Proposto 10.6
Enunciado: Escreva um programa para registrar os seguintes dados de uma frota de veículos de uma empresa:
Placa (string – chave – obrigatório todas as letras maiúsculas)
Marca
Modelo
Tipo (caminhão, furgão, automóvel, motocicleta, etc)
Kilometragem
Data da Compra (string no formato AAAAMMDD – ano,mês,dia)
O programa deve ficar em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM para a placa. 
Se for digitada uma placa com letras minúsculas o programa deve convertê-las para maiúsculas com o método .upper().
Para cada veículo leia todos os dados e carregue em um dicionário. 
Se uma placa já existente for digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração em algum dado basta digitar o novo valor. 
Para os campos em que nada for digitado deve ser mantido o valor já cadastrado.
Ao final do laço mostre os dados na tela com uma formatação legível.
Desafio Inclua no programa uma validação da placa, seguindo as seguintes regras:
a)Deve ter 7 caracteres
b)Os três primeiros devem ser letras
c)Os caracteres 4, 6 e 7 devem ser algarismos
d)O caractere 5 pode ser número (placa antiga) ou letra (nova placa padrão Mercosul)
"""
print('<<-Frota de Veículos->>')
dicFrota = {}

while True:
    placa = input('Digite a placa do carro: ').upper()  
    if placa == 'FIM':
        print('Fim do programa')
        break

    elif placa in dicFrota:
        dados_antigos = dicFrota[placa]
        print(f'A  placa {placa} já foi digitada')
        msg = input('Deseja alterar s/n: ').upper()
        if msg=='S':
           
            print("\n--- MODO DE ATUALIZAÇÃO ---")
            #--- Marca ---
            print(f"Marca Actual:{dados_antigos['marca']}")
            nova_marca = input('Nova marca (Deixa vazio para manter): ')
            if nova_marca != '':
                dados_antigos['marca'] = nova_marca
            #--- Modelo ---
            print(f"Modelo Actual:{dados_antigos['modelo']}")
            novo_modelo = input('Novo modelo (Deixa vazio para manter):')
            if novo_modelo != '':
                dados_antigos['modelo'] = novo_modelo
            #--- Tppo ---
            print(f"Tipo Actual:{dados_antigos['tipo']}")
            novo_tipo = input('Novo tipo (Deixa vazio para manter):')
            if novo_tipo != '':
                dados_antigos['tipo'] = novo_tipo 
            #--- Kilometragem ---
            print(f"Kilometragem Actual:{dados_antigos['km']}")
            novo_km = input('Novo km (Deixa vazio para manter):')
            if novo_km != '':
                dados_antigos['km'] = novo_km
            #--- Data compraal ---
            print(f"Data Actual:{dados_antigos['dataCompra']}")    
            novo_data = input('Nova data de compra (Deixa vazio para manter):')
            if novo_data != '':
                dados_antigos['dataCompra'] = novo_data
   
    else:
        
        marca = input('Digite a marca: ')
        modelo = input('Digite o modelo: ')
        tipo = input('Digite o tipo: ')
        km= input('Digite os km: ')
        dataCompra = input('Digite a data da compra: ')
        dicItem = {'marca':marca, 'modelo':modelo, 'tipo':tipo, 'km':km, 'dataCompra':dataCompra}
        dicFrota[placa] = dicItem
print('{:15} {:15} {:15} {:15} {:15} {:>15}'.format('Placa', 'Marca', 'Modelo', 'Tipo', 'Kilometragem', 'Data da Compra'))
for placa, dados in dicFrota.items():
    print('{:15} {:15} {:15} {:15} {:15} {:15}'.format(placa, dados['marca'], dados['modelo'], dados['tipo'], dados['km'], dados['dataCompra']))

