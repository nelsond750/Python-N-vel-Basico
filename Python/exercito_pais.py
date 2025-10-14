nome  = input('Digite o nome da pessoa: ')
idade = int(input('Digite a idade'))
sexo  = input('Digite o sexo: ')

if sexo == 'f' or sexo == 'F':
    if idade >= 21 and idade <= 34:
        print(nome,'Será aceite para o serviço militar')
    else:
        print('Não será aceite para o serviço militar')
elif sexo == 'm' or sexo == 'M':
    if idade>= 18 and idade <= 39:
        print(nome,'Será aceite para o serviço militar')
    else:
        print(nome,'Não será aceito para o serviço militar')
else:
    print('Sexo inválido')

