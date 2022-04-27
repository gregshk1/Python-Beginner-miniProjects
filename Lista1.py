
lista = []
for i in range(0, 5):
    lista.append(int(input('Digite valores: ')))

print(f'A lista é composta por {lista} números')
print(f'O maior valor é {max(lista)} e o menor é o {min(lista)}')
print(f'A posição do maior valor na lista é {lista.index(max(lista)) + 1}')
print(f'A posição do menor valor na lista é {lista.index(min(lista)) + 1}')
