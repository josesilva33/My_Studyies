'''catop = float(input('Quanto mede o cateto oposto: '))
catad = float(input('Quanto mede o cateto adjacente: '))
calculo = (catop ** 2 + catad ** 2 ) ** (1/2)
print('A hipotenusa dos dois catetos é {:.2f}'.format(calculo))'''

import math
catop = float(input('Quanto mede o cateto oposto: '))
catad = float(input('Quanto mede o cateto adjacente: '))
calculo = math.hypot(catop, catad)
print('A hipotenusa dos dois catetos é {:.2f}'.format(calculo))
