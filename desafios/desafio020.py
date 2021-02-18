from random import shuffle
print('='*10, 'Desafio 020', '='*10, '\nSorteio\n')

alunos = [input('Informe o nome do primeiro aluno: '), input('Informe o nome do segundo aluno: '),
          input('Informe o nome do terceiro aluno: '), input('Informe o nome do quarto aluno: ')]
shuffle(alunos)
print(f'A ordem de apresentação é: {alunos}')
