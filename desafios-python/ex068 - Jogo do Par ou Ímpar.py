from random import randint
while True:
    print('PAR OU ÍMPAR')
    print('=-'*30)
    cont = 0
    pi = ' '
    num = int(input('Diga um valor: '))
    while pi not in 'pi':
        pi = input('Par ou Ímpar? [P/I] ').lower()
    pc = randint(0,11)
    res = num + pc
    print(f'Você jogou {num} e o computador {pc}. Total de {res}. ', end='')
    print('DEU PAR' if res % 2 == 0 else 'DEU ÍMPAR')
    if res % 2 == 1:
        if pi == 'i':
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        if pi == 'p':
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')  
    
    