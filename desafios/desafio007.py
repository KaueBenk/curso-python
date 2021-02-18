print('='*10, 'Desafio 007', '='*10)
print('Média de um aluno\n')

input_nota_1 = float(input('Informe a primeira nota: '))
input_nota_2 = float(input('Informe a segunda nota: '))

print('\nVocê informou: {} e {}'.format(input_nota_1, input_nota_2))
print('\nA média de notas desse aluno é {:.1f}'.format((input_nota_1 + input_nota_2) / 2))
