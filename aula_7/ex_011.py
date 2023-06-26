larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua paarede tem a dimensao de {} x {} e sua area é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar esta area voce precisará de {}L de tinta.'.format(tinta))
