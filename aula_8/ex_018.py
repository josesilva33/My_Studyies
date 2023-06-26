import math
ang = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O angulo {}\ntem o seno {:.2f}\no cosseno {:.2f}\ne o Tangente {:.2f}'.format(ang, seno, cos, tan))