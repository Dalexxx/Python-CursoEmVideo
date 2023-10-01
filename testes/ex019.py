import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceira aluno: ')
aluno4 = input('Quarto aluno: ')

nomes = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(nomes)

print(f'O aluno escolhido foi {escolhido}')