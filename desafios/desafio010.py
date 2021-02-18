dolar = 5.56
s = '='*10

print(f'{s} Desafio 010 {s}\nDólares na carteira\nConsiderando dolar a R${dolar}\n')

in_carteira = float(input('Informe quantos reais você tem na carteira: R$'))
print(f'\nVocê pode comprar {round(in_carteira / dolar, 2)} dolares')
