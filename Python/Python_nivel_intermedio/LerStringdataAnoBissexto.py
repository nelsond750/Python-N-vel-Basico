#Recebe String 
S = input('Digite a string no formato aaaammdd: ')

if len(S) == 8 and S.isnumeric():
#Fatiamento para extrair as partes (se a validação for True)
    ano = S[:4]
    mes = S[4:6]
    dia = S[6:]
    if int(ano) % 4 == 0:  
        print('O ano é bissexto')   
#Saída no formato dd/mm/aaaa~     
    else:
        print('O ano não é bissexto') 
    print(f'A data fornecida é: {dia}/{mes}/{ano}') 
else:
#Mensagem de erro (se a validação for False)
    print('Erro! apenas numeros inteiros.') 