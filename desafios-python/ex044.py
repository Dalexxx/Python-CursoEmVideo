print(f'{"Lojas Gunabara":=^40}')
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão ')
opção = int(input('Qual é a opção? '))

if opção == 1:
    print(f'Sua compra de R${preço} vai custar R${preço - (preço*0.10):.2f} no final.')
elif opção == 2:
    print(f'Sua compra de R${preço} vai custar R${preço - (preço*0.05):.2f} no final.')
elif opção == 3:
    print(f'Sua compra será parcelada em 2x de R${preço / 2:.2f} SEM JUROS')
    print(f'Sua compra de R${preço} vai custar R${preço:.2f} no final.')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preço + (preço*0.20)
    print(f'Sua compra será parcelada em {parcelas}x de R${juros / parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preço} vai custar R${preço + (preço*0.20):.2f} no final.')
else:
    print(f'OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')