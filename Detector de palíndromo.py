pala = str(input('Digite uma palavra ou frase para descobrir se ela é um palíndromo: ')).strip().upper()
palal = pala.split()
junto = ''.join(palal)
inverso = ''
for letra in range(len(junto) -1 , -1 , -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')