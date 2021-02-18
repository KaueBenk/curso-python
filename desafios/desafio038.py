print('='*10, 'Desafio 038', '='*10, '\nComparação de números\n')

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if num1 > num2:
    print('\nO primeiro valor é maior.')
elif num2 > num1:
    print('\nO segundo valor é maior.')
else:
    print('\nNão existe valor maior, os dois são iguais.\n')
