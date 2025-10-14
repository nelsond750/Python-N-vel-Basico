# Cálculo od IMC, ìndice da massa corporal.
print('Inicio do programa')
Peso = float(input('Digite o Peso: '))
Altura = float(input('Digite a altura da pessoa: '))

IMC = Peso/Altura**2
if IMC < 18.5:
    print(f'A baixo do peso {IMC}')
elif IMC >= 18.5 and IMC <= 24.9:
    print(f'Peso Normal {IMC}')
elif IMC <= 25 and IMC <= 30:
    print(f'Sobre Peso {IMC}')
else:
    print(f'obeso {IMC}')
print('Fim do programa')