while True:
    string = input('Digite uma string: ')
    if string == 'FIM':
        print('Programa encerrado.')
        break
    print(f'A string digitada é: {string} o tamanho é: {len(string)}')
