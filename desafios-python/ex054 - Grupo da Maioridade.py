from datetime import date
maior = 0
menor = 0
atual = date.today().year
for c in range(1,8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu?'))
    if ano > atual - 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
