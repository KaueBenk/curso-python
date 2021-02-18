print('='*10, 'Desafio 024', '='*10, '\nCidade com Santo\n')
in_cidade = input('Informe o nome de uma cidade: ').strip()
print(f'O nome da cidade começa com santo? {"santo" in in_cidade.split()[0].lower()}')
