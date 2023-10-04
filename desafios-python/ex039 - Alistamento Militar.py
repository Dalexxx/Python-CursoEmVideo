from datetime import date
ano = int(input('Anos de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
calculo = anoatual - ano - 18
print(f'Quem nasceu em {ano} tem {idade} anos em {anoatual}.')
if idade == 18:
    print('Você deve se alistar imediatamente')
    print(f'Seu alistamento é em {anoatual}')
elif idade > 18:
    print(f'Voce já deveria ter se alistado há {idade - 18} anos')
    print(f'Seu alistamento foi em {anoatual - calculo}')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será em {ano + 18}')
