# Programa que lê uma string e informa o tamanho dela. O programa encerra quando o usuário digitar "FIM".

string = input('Digite uma string: ')
while  True:
    if string != 'FIM':
        print(f'A string digitada é: {string} o tamanho é: {len(string)}')
        string = input('Digite uma string: ')
    else:
        if string == 'FIM':
            print('Programa encerrado.')            
        break
       
    
   
    
    