print('='*10, 'Desafio 044', '='*10, '\nCalculo Condições de Pagamento\n')

preco = int(input('Informe o preço normal do produto: '))

condicao = str(input('''
Informe a condição de pagamento
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mias no cartão: 20% de juros

Escolha uma opção: '''))

print('')

if "1" in condicao:
    print(f'O valor final do produto será R$ {round(preco * 0.9, 2)}')
elif "2" in condicao:
    print(f'O valor final do produto será R$ {round(preco * 0.95, 2)}')
elif "3" in condicao:
    print(f'O valor final do produto será R$ {preco}, em duas parcelas de R$ {round(preco / 2, 2)}.')
elif "4" in condicao:
    parcelas = int(input('Em quantas vezes(parcelas)? '))
    print(f'\nO valor final do produto será R$ {round(preco * 1.2)}, em {parcelas} parcelas de R$ {round(preco / parcelas, 2)}')
print('')
