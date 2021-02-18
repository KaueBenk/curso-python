from random import randint
from time import sleep

print('='*10, 'Desafio 045', '='*10, '\nJokenpô\n')

usr = int(input('''Escolha sua jogada
1 - Pedra
2 - Papel
3 - Tesoura

Selecione uma jogada: '''))
pc = int(randint(1, 3))

jogadas = {
    1: "pedra",
    2: "papel",
    3: "tesoura"
}

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('')
if usr == pc:
    print('EMPATE! Você e o computador estão interligados.')
elif usr == 1 and pc == 3 or usr == 2 and pc == 1 or usr == 3 and pc == 2:
    print(f'VOCÊ VENCEU!!!\nVocê jogou {jogadas[usr]} e o computador jogou {jogadas[pc]}.')
else:
    print(f'Você perdeu :/ o computador foi mais esperto e aniquilou seu(a) {jogadas[usr]} com o(a) {jogadas[pc]} dele.')
