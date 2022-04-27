import math
a = float(input('Insira o valor do ângulo qual deseja calcular o seno cosseno e tangente: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno é {:.2f}, o cosseno {:.2f} e a tangente {:.2f} do ângulo {}'.format(s, c, t, a))