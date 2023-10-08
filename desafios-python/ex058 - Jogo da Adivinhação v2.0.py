from random import randint
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
pc = randint(0,10)
palpite = int(input('Qual é seu palpite? '))
tot = 1
while palpite is not pc:
    tot += 1   
    if pc > palpite:
        print('Mais... Tente mais uma vez.')
    if pc < palpite:
        print('Menos... Tente mais uma vez.')
    palpite = int(input('Qual é seu palpite? '))
print(f'Acertou com {tot} tentativas. Parabéns!')