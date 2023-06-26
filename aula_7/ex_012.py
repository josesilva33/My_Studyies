valor = float(input('Qual é o preço do produto? R$'))
calculo = valor - (valor * 5 / 100)
print('O produto que custava {} na promoçao com desconto de 5% vai custar R${:.2f}'.format(valor, calculo))
