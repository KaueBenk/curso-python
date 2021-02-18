from datetime import date

print('='*10, 'Desafio 039', '='*10, '\nIdade de Alistamento\n')

sexo = int(input('''Informe o seu sexo:
1 - Homem
2 - Mulher

Escolha uma opção: '''))

if sexo == 1:
    ano = int(input('Informe o seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        print(f'Em {18-idade} anos você vai se alistar ao serviço militar.')
    elif idade == 18:
        print('Já é a hora de se alistar!')
    else:
        print(f'Já se passaram {idade-18} anos do seu tempo de alistamento.')
else:
    print('Mulheres não precisam se alistar :).')