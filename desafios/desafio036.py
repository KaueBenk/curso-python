print('='*10, 'Desafio 036', '='*10, '\nAnálise de Empréstimo\n')

salario = int(input('Informe o salário: '))
valor_casa = int(input('Informe o valor da casa: '))
anos = int(input('Informe a quantidade de anos para pagar a casa: '))

prestacao = valor_casa / anos / 12
porcentagem_do_salario = prestacao / salario * 100

if porcentagem_do_salario > 30:
    print(f'Empréstimo negado, o valor da prestação (R$ {round(prestacao, 2)}) excedeu o limite de 30% do seu salário.')
else:
    print(f'Empréstimo aprovado! O valor da prestação (R$ {round(prestacao, 2)}) não excedeu o limite de 30% do seu salário.')
