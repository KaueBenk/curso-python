print('='*10, 'Desafio 029', '='*10, '\nMulta\n')
vel = int(input('Informe a velocidade do carro: '))
if vel > 80:
    print('Você ultrapassou 80km/h e foi multado.\n'
          f'Valor da multa: R${(vel - 80) * 7:.2f}.')
else:
    print('Você não ultrapassou 80km/h e não foi multado, parabéns!')
