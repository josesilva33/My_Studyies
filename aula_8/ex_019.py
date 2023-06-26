import random
num1 = input('Primeiro aluno:')
num2 = input('Segundo aluno:')
num3 = input('Terceiro aluno:')
num4 = input('Quarto aluno:')
lista = [num1, num2, num3, num4]
result = random.choice(lista)
print('O aluno escolhido foi {}'.format(result))

'''A tecla [] serve para fazer listas, e ramdom para fazer coisas aleatórias'''