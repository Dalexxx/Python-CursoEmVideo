nota1 = float(input('Primeiro nota: '))
nota2 = float(input(f'Segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média foi {media} e você está reprovado')
elif media >= 7:
    print(f'Sua média foi {media} e você está aprovado')
else:
    print(f'Sua média foi {media} e você está de recuperação')
