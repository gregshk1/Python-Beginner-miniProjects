r1 = float(input('Digite o primeiro lado do triângulo: '))
r2 = float(input('Agora o segundo lado: '))
r3 = float(input('Agora o terceiro: '))

if r1 == r2 == r3:
    print('É um triângulo equilátero')
elif r1 != r2 and r1 != r2 and r2 != r3:
     print('É um triângulo escaleno')
else:
    print('É um triângulo isósceles')

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('As medidas que digitou podem formar um triângulo')
else:
    print('As medidas fornecidas não podem formar um triângulo')
