#frase = str(input('Digite uma frase: ')).upper().strip()

#print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
#print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
#print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(nome[0],nome[-1]))