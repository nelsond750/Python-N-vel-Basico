salario = float(input('Digite o salrio: '))
parcela = float(input('Digite o valor da parcela: '))
percentagem= (8*salario)/100
if parcela < percentagem:
    print('Emprestimos concedido')
else: 
    print('Emprestimo não concedido')
