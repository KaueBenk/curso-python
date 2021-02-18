print('='*10, 'Desafio 037', '='*10, '\nConversão de Bases Numéricas\n')

num = int(input('Insira um número decimal: '))
base = str(input('''\nInforme a base para qual deseja converter
1 para converter para binário
2 para converter para octal
3 para converter para hexadecimal

Escolha uma opção: '''))

if "1" in base:
    num_cvt = bin(num)
elif "2" in base:
    num_cvt = oct(num)
elif "3" in base:
    num_cvt = hex(num)
else:
    print('Esta opção não existe\n')

print(f'\nO número {num} na base escolhida é {num_cvt[2:]}\n')
