nome  = (input('Digite o nome do estudante'))
nota1 =float(input('Digite a primeira nota:'))
nota2 =float(input('Digite a primeira nota:'))
nota3 =float(input('Digite a primeira nota:'))
media = (nota1+nota2+nota3)/3

if media >= 7.0:
    print(f'nome: {nome}, media:{media:.3f}, Aprovado')
else:
    print(f'nome: {nome}, media:{media:.3f}, Reprovado')