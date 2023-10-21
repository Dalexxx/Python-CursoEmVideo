print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
tot = prod = menor = cont = 0
p = 1000
while True:
    nome = input('Nome do Produto:')
    preço = int(input('Preço: R$'))
    cont += 1
    tot += preço
    if preço > p:
        prod += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    again = ' '
    while again not in 'sn':
        again = input('Quer continuar? [S/N] ').lower().strip()[0]
    if again == 'n':
        break
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {prod} produtos custando mais do que {p:.2f}')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')