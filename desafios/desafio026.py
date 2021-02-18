print('='*10, 'Desafio 026', '='*10, '\nAnálise de Frase\n')
in_frase = str(input('Informe uma frase: ')).strip()
print(f'A letra "A" aparece na frase {in_frase.lower().count("a")} vezes.\n'
      f'A letra "A" aparece pela primeira vez na posição {in_frase.lower().find("a")}.\n'
      f'A letra "A" aparece pela última vez na posição {in_frase.lower().rfind("a")}.')
