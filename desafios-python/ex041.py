from datetime import date
nascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual-nascimento
print(f'O atleta tem {idade} anos.')

if idade <= 9:  
    print('Classificação MIRIM')
elif idade <= 14:
    print('Classificação INFANTIL')
elif idade <= 19:   
    print('Classificação JUNIOR')
elif idade <= 25:   
    print('Classificação SÊNIOR')
else:
    print('Classificação MASTER')

