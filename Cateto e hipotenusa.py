import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.hypot(co, ca)
print('A hipotenusa é: {:.2f}'.format(hip))