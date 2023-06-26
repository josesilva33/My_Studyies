dias = float(input('Imforme quantos dias o carro foi alugado: '))
km = float(input('Informe quantos quilómetros o carro percorreu: '))
cal1 = (dias * 60) + (km * 0.15)
print('O aluguel do carro custa {:.2f}'.format(cal1))
