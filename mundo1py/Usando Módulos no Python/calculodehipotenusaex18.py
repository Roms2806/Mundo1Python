
'''co = int(input('Digite um valor para o cateto oposto:'))
ca = int(input(' Digite um valor para o cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Calculando a hipotenusa, a²+b²=c², seu comprimento vale {:.3f}'.format(hi))'''

from math import hypot
co = int(input(" Digite um valor para o cateto oposto:"))
ca = int(input(' Digite um valor para o cateto adjacente:'))
print('Calculando a hipotenusa seu valor é {}'.format(hypot(co, ca)))
