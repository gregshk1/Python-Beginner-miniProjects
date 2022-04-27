soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        contador = contador + 1
print(soma, contador)

