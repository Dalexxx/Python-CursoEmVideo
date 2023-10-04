salario = float(input('Qual o seu salário atual: '))

salario15 = (salario * 0.15) + salario
salario10 = (salario * 0.10) + salario

if salario <= 1250:
    print(f'O seu novo salário é R${salario15:.2f}')

else:
    print(f'O seu novo salário é R${salario10:.2f}')
