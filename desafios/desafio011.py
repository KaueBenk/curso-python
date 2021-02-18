s = '='*10

print(f'{s} Desafio 011 {s}\nPintura de parede\n')

in_altura = float(input('Informe a altura da parede em metros: '))
in_largura = float(input('Informe a largura da parade em metros: '))

print(f'\nA área da parede é: {in_altura*in_altura} m²\nSão necessários {in_largura * in_altura / 2} litros de tinta')
