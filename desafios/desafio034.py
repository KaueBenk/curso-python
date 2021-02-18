print('='*10, 'Desafio 034', '='*10, '\nAumento de Salário\n')
sal = int(input('Informe o salário do funcionário: '))

if sal > 1250:
    print(f'O aumento deve ser de R${sal * 0.1} logo, o novo salário é R${sal * 0.1 + sal}')
else:
    print(f'O aumento deve ser de R${sal * 0.15} logo, o novo salário é R${sal * 0.15 + sal}')
