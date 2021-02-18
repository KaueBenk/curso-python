print('=' * 10, 'Desafio 023', '=' * 10, '\nAnalise de Números\n')
in_num = int(input('Informe um número de 0 a 9999: '))
print(f'Utilizando matemática:\n'
      f'Unidade: {in_num // 1 % 10}\n'
      f'Dezena: {in_num // 10 % 10}\n'
      f'Centena: {in_num // 100 % 10}\n'
      f'Milhar: {in_num // 1000 % 10}')
