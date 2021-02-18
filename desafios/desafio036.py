print('='*10, 'Desafio 036', '='*10, '\nAnálise de Empréstimo\n')

salario = float(input('Informe o salário: R$ '))
valor_casa = float(input('Informe o valor da casa: R$ '))
anos = int(input('Informe a quantidade de anos para pagar a casa: '))
prestacao = valor_casa / anos / 12

print('')
if salario * 0.3 < prestacao:
    print(f'Empréstimo negado, o valor da prestação (R$ {round(prestacao, 2)}) excedeu o limite de 30% do seu salário.')
else:
    print(f'Empréstimo aprovado! O valor da prestação (R$ {round(prestacao, 2)}) não excedeu o limite de 30% do seu salário.')
