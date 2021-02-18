print('='*10, 'Desafio 027', '='*10, '\nAnálise de Nome\n')
in_nome = str(input('Informe seu  nome completo: ')).strip().title()
nome = in_nome.split()
print(f"Seu primeiro nome é {nome[0]}.\n"
      f"Seu último nome é {nome[len(nome)-1]}.")
