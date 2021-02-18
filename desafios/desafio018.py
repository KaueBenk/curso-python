from math import sin, cos, tan, radians

print('='*10, 'Desafio 018', '='*10, '\nSeno, cosseno e tangente\n')

in_ang = radians(float(input('Informe o ângulo: ')))

print(f'Seno: {sin(in_ang):.2f}\nCosseno: {cos(in_ang):.2f}\nTangente: {tan(in_ang):.2f}')
