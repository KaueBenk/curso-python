from datetime import date

print('='*10, 'Desafio 041', '='*10, '\nCategorização de Atletas\n')

ano = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print('')

if idade <= 9:
    print('O atleta pertence à categoria mirim.')
elif idade <= 14:
    print('O atleta pertence à categoria infantil.')
elif idade <=19:
    print('O atleta pertence à categoria junior.')
elif idade <= 20:
    print('O atleta pertence à categoria sênior.')
else:
    print('O atleta pertence à categoria master.')
print('')
