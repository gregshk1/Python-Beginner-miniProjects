num = int(input('Descubra se o número é primo: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\nO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Logo {} é primo'.format(num))
else:
    print('Logo {} não é primo'.format(num))
