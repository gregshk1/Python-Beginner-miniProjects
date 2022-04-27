print('-----SUPER BARATÃO-----')
item = quantidade = novac = precoItem10 = total = menorPreco = cont = 0


while True:
    novac = str(input('Deseja comprar alguma coisa?? S/N: ')).strip().upper()
    if novac in 'S':
        item = str(input('Qual o nome do produto? '))
        preco = float(input('Qual o preço do produto em reais? R$:  '))
        cont += 1
        if cont == 1:
            menorPreco = preco
        quantidade = int(input('Qual a quantidade, 1, 2, 3...:  '))
        total = (preco * quantidade) + total
        if preco > 10000:
            precoItem10 += 1
    elif novac in 'N':
        print(f'O total da compra foi {total}, {precoItem10} produto(s) custam mais de R$10.000 e o produto mais barato é o(a) {menorPreco}.')
        break
