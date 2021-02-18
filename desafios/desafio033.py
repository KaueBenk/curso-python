print('='*10, 'Desafio 033', '='*10, '\nAnálise de Números\n')
num = [int(input('Informe o primeiro número: ')),
       int(input('Informe o segundo número: ')),
       int(input('Informe o terceiro número: '))]

num.sort(reverse=True)
print(f'\nO maior número é {num[0]}\n'
      f'O menor número é {num[2]}')
