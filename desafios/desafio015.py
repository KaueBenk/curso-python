print('='*10, 'Desafio 015', '='*10, '\nAluguel de carro\n')

in_dias = int(input('Informe quantos dias o cliente ficou com o carro: '))
in_km = float(input('Informe quantos quilometros foram rodados com o carro: '))

print(f'\nO valor total do aluguel é R${in_dias * 60 + in_km * 0.15:.2f}')
