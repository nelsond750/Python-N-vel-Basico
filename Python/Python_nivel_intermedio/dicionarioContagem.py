diciContagem = {}

while True:
    try:

        nInteiro = int(input('Digite os números (1 a 9, ou 0/- para sair):'))

    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')
        continue
   
    if  nInteiro <= 0:
        print('Fim do programa...')
        break
    elif 1 <= nInteiro <= 9:
        if  nInteiro in diciContagem:
            
          diciContagem[nInteiro]+= 1
          
        else:
            diciContagem[nInteiro] = 1
    else:
        print('Valor fora do intervalo [1-9]. Ignorado.')
        continue
for numero, frequencia in diciContagem.items():
    print(f'O número: {numero} foi digitado {frequencia} vez.')
print('Fim do programa...')
