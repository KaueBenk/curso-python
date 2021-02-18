from random import choice
print('='*10, 'Desafio 019', '='*10, '\nSorteio\n')

in_aluno1 = str(input('Informe o nome do primeiro aluno: '))
in_aluno2 = str(input('Informe o nome do segundo aluno: '))
in_aluno3 = str(input('Informe o nome do terceiro aluno: '))
in_aluno4 = str(input('Informe o nome do quarto aluno: '))

alunos = [in_aluno1, in_aluno2, in_aluno3, in_aluno4]

print(f'O aluno {choice(alunos)} apagará o quadro.')
