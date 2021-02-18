from math import hypot

print('='*10, 'Desafio 017', '='*10, '\nCalculadora de hipotenusa\n')

in_co = float(input('Informe o cateto oposto: '))
in_ca = float(input('Informe o cateto adjacente: '))

print(f'O comprimento da hipotenusa deste triângulo retângulo é {hypot(in_co, in_ca):.2f}')
