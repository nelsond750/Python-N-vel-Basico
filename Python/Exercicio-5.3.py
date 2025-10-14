numero = int(input("Digite um número entre 100 e 200: "))
while True:
    numero = int(input("Digite um número entre 100 e 200: "))
    if 100 <= numero <= 200:
        print("Valor aceito.")
        break
    else:
        print("Valor inválido. Tente novamente.")
        
