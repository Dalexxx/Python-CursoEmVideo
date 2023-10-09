num = int(input('Digite um número para calcular seu Fatorial: '))
tot = num
while tot is not 1:
    
    tot -= 1
    print(f'{tot}', end='')
    print(' x ' if tot > 1 else ' = ', end='')

    num = num * tot   
    
print(num)
