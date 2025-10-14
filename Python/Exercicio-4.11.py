PrecoCusto = float(input('Digite o preço do custo do produto: '))
if PrecoCusto <= 100:
    PrecoVenda = PrecoCusto + (45*PrecoCusto)/100

    print(f'O precço de venda é: {PrecoVenda:.2f}')
else:
    if PrecoCusto > 100:
        PrecoVenda = PrecoCusto +(35*PrecoCusto)/100
        print(f'O preco de venda é: {PrecoVenda:.2f}')