num = maior = menor = []


for c in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))

for p, v in enumerate(num):
    if v == max(num):
        maior.append(p)
    if v == min(num):
        menor.append(p)

print(f'Você digitou os valores {num}')
print(f'O maior valor foi o {max(num)} na posições {maior}')
print(f'O menor valor foi o {min(num)} nas posições {menor}')



'''num = []
cont = maior = menor = 0
for n in range(0,5):
    num.append(int(input('Digite um número:')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] > maior:
            maior = num[n]
        if num[n] < menor:
            menor = num[n]

print(f'Voce digitou os valores {num}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')'''

