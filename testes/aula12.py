nome = str(input('\nQual é o seu nome? ')).capitalize()

if nome == 'Gustavo':
    print('\nQue nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\nSeu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\nBelo nome feminino!')
else:
    print('\nSeu nome é bem normal.')

print(f'Tenha um bom dia {nome}\n')
