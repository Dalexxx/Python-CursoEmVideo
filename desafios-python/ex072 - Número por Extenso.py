ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 10: '))
        if 0 <= num <= 10:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {ext[num]}')
    
    while True:
        again = input('Você quer continuar? [S/N] ').upper()
        if again in 'SN':
            break
    if again == 'N':
        break
print('Fim do programa')






'''-----------MY WAY------------
num = int(input('Digite um número entre 0 e 10: '))
tot = 0
while num < 0 or num > 10:
    print('Tente novamente. ', end='')
    num = int(input('Digite um número entre 0 e 10: '))
for cont in range(0, len(ext)):
    if num == tot:
        print(f'Você digitou o número {ext[cont]}')
    tot += 1'''
    


