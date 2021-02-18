print('='*10, 'Desafio 031', '='*10, '\nPreço da Passagem\n')
dis = float(input('Informe a distância em Km da viagem: '))
if dis <= 200:
    print(f'Preço da passagem: R${dis * 0.5:.2f}.')
else:
    print(f'Preço da passagem: R${dis * 0.45:.2f}.')
