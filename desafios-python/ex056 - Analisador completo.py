'''desenvolva um programa que leia o nome,
idade e sexo de 4 passoas e mostre:
-a média de idade do grupo *
-qual é o nome do homem mais velho
-quantas mulheres tem menos de 20 anos'''
media = 0
mulher = 0
nomeolder = ''
maior = 0
for c in range(1,5):
    print(f'----- {c}° PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    if sexo in 'Ff' and idade <= 20:
        mulher += 1
    media += idade
    if c == 1 and sexo == 'M':
        maior = idade
        nomeolder = nome
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            nomeolder = nome

    
print(f'A média de idade do grupo é de {media/4} anos')
print(f'O mais velho tem {maior} anos e seu nome é {nomeolder}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos')




