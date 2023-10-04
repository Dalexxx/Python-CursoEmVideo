valor = int(input('Valor da casa: R$'))
salario = int(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

print(f'Para pagar uma casa de R${valor} em {anos} anos a prestação será de R${valor/(anos*12):.2f}')

if valor/(anos*12) > salario*0.30:
    print('Empréstimo NEGADO!')
else:
    print('Emprestimo pode ser CONCEDIDO!')