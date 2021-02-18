print('='*10, 'Desafio 022', '='*10, '\nStrings\n')
in_nome = str(input("Qual o seu nome completo? ")).strip()
print(f'Seu nome com todas as letras maiúsculas: {in_nome.upper()}\n'
      f'Seu nome com todas as letras minúsculas: {in_nome.lower()}\n'
      f'Seu nome completo tem {len("".join(in_nome.split()))} letras.\n'
      f'Seu primeiro nome tem {len(in_nome.split()[0])} letras.')
