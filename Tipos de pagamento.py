from time import sleep
print('{:=^40}'.format(' SUPER MERCADO '))
preco = float(input('Preço das compras:R$ '))
pag = print('''Como deseja pagar? 
[ 1 ] à vista no dinheirou ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual a opção? '))


if op == 1:
    avdc = preco - (preco*0.1)
    print('Pagamento à vista ou em cheque, preço de {:.2f} com 10% de desconto aplicado'.format(avdc))
elif op == 2:
    avc = preco - (preco*0.05)
    print('Pagamento à vista no cartão, preço de {:.2f} com desconto de 5% aplicado'.format(avc))
elif op == 3:
    xc = preco
    parc = preco / 2
    print('Dividido no cartão em 2x, preço de {:.2f} duas parcelas de {:.2f}'.format(xc, parc))
elif op == 4:
    mvz = int(input('Quantas vezes deseja dividir? '))
    xc2 = (preco * 0.2) + preco
    parc2 = xc2 / mvz
    print('Dividido em {:.0f} ou mais vezes no cartão, preço de {:.2f} com parcelas de {:.2f}'.format(mvz, xc2, parc2))