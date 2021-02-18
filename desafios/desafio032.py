from datetime import date

print('='*10, 'Desafio 032', '='*10, '\nAno Bissexto\n')
ano = str(input('Informe um ano: '))
int_ano = int(0)

if ano != '':
    int_ano = int(ano)

if int_ano == 0 or ano == '':
    int_ano = date.today().year

if (int_ano % 4 == 0 and int_ano % 100 != 0) or (int_ano % 400 == 0):
    print(f'O ano {int_ano} é bissexto.')
else:
    print(f'O ano {int_ano} não é bissexto.')
