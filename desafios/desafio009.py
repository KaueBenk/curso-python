print('='*10, 'Desafio 009', '='*10, '\nTabuada')

in_num = round(float(input('\nInforme um número: ')), 2)

print('-'*18)
for x in range(0, 11):
    print(f'{in_num} * {x:>2} = {round(x * in_num, 2)}')
print('-'*18)
