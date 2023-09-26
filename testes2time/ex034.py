salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    print(f'Quem ganhava {salario} passa a ganhar R${(salario*0.15) + salario:.2f}')
else:
    print(f'Quem ganhava {salario} passa a ganhar R${(salario*0.10) + salario:.2f}')
