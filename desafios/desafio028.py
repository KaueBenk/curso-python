from random import randint
print('='*10, 'Desafio 028', '='*10, '\nAdivinhação de Números\n')
num = randint(0, 5)
usr_num = int(input('Tente adivinhar em qual número de 0 a 5 o computador "pensou": '))
if usr_num == num:
    print(f'Você acertou! O computador "pensou" no número {num}.')
else:
    print(f'Você errou. O computador "pensou" no número {num}.')
