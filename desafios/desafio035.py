print('='*10, 'Desafio 035', '='*10, '\nAnálise de Retas\n')
ret = [float(input('Informe o valor da primeira reta: ')),
       float(input('Informe o valor da segunda reta: ')),
       float(input('Informe o valor da terceira reta: '))]

ret.sort()
if (ret[1] - ret[0]) < ret[2] < (ret[1] + ret[0]):
    print('\nVocê pode formar um triângulo com essas retas.')
else:
    print('\nVocê não pode formar um triângulo com essas retas.')
