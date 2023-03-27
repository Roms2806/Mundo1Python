'''import math
num = float(input('Digite um número: '))
print('sua porção inteira é {}'.format(math.trunc(num)))

num = float(input('Digite um valor: '))
n = int(num)
print('A parte inteira do valor {} corresponde a {}'.format(num, n))'''

from math import trunc
num = float(input('Digite um valor: '))
print('A porção inteira do valor {} é {}'.format(num, trunc(num)))