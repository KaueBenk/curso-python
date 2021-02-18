print('='*10, 'Desafio 040', '='*10, '\nMédia de Notas\n')

nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota:'))

media = round((nota1 + nota2) / 2, 2)

print('')
if media < 5:
    print(f'O aluno esta REPROVADO com média {media}.')
elif media <= 6.9:
    print(f'O aluno esta de RECUPERAÇÃO com média {media}.')
elif media <= 10:
    print(f'O aluno esta APROVADO com média {media}.\n')
else:
    print(f'Inteligente demais! O aluno esta APROVADO com média {media}')
