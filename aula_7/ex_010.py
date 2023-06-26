print('Olá seja bem vindo ao nosso novo programa, aqui voce pode ver quanto está custando qualquer moeda que voce deseja em tempo real')
real = float(input('quanto dinheiro voce tem na carteira?: R$'))
dolar = real / 4.77
Euro = real / 5.21
Iene = real / 0.03
Libra = real / 6.10
Peso = real / 0.019
print('Com R${:.2f} reais voce pode comprar\nUS${:.2f} Dolares'.format(real, dolar))
print('EU${:.2f} Euros'.format(Euro))
print('JP${:.2f} Ienes'.format(Iene))
print('GB${:.2f} Libras'.format(Libra))
print('MX${:.2f} Pesos'.format(Peso))
