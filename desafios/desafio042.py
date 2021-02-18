print('='*10, 'Desafio 042', '='*10, '\nCategorização de Atletas\n')

ret = [float(input('Informe o valor da primeira reta: ')),
       float(input('Informe o valor da segunda reta: ')),
       float(input('Informe o valor da terceira reta: '))]

ret.sort()
if (ret[1] - ret[0]) < ret[2] < (ret[1] + ret[0]):
    print('\nVocê pode formar um triângulo com essas retas.')
    if ret[0] == ret[1] == ret[2]:
        print('O triângulo formado será equilátero.')
    elif ret[0] == ret[1] or ret[1] == ret[2] or ret[2] == ret[0]:
        print('O triângulo formado será isóseles.')
    else:
        print('O triângulo formado será escaleno.')
else:
    print('\nVocê não pode formar um triângulo com essas retas.')
print('')
