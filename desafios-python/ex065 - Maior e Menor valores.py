continuar = True
cont = tot = maior = menor = 0
while continuar:
    num = int(input('Digite um número:'))
    cont += 1
    tot += num
    if cont == 1:
        maior = menor = num
        print()
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    con = input('Quer continuar? [S/N] ').lower()
    if con == 'n':
        continuar = False
print(f'Você digitou {cont} números e a média foi {tot/cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
    