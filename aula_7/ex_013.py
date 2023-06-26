valor = float(input('preço do produto:'))
vis = valor - (valor * 10 / 100)
car = valor + (valor * 8 / 100)
print('O produto a vista sairá por {} com 10% de desconto\n'
      'E o produto no cartao sairá por {} com 8% de acrecimo.'.format(vis, car))
