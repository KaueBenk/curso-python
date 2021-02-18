print('='*10, 'Desafio 043', '='*10, '\nCalculo de IMC\n')

peso = int(input('Informe seu peso: '))
altura = int(input('Informe sua altura em metros: '))

imc = round(peso / altura^2, 2)

print('')
if imc <= 18.5:
    print(f'Seu IMC é {imc}, oque significa que você esta abaixo do peso ideal.')
elif imc <= 25:
    print(f'Seu IMC é {imc}, oque significa que você esta com o peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é {imc}, oque significa que você esta com sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC é {imc}, oque significa que você esta obeso.')
else:
    print(f'Seu IMC é {imc}, oque significa que você esta com obesidade móbida.')
print('')
