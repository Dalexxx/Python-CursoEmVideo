soma = 0 
cont = 0

for c in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Você digitou {cont} numeros pares, e a soma deles é {soma}')
